# backend/routes/report.py

import io
from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse

from backend.services.report_service import generate_report

router = APIRouter(tags=["report"])


@router.get("/report/{region}", responses={200: {"content": {"application/pdf": {}}}})
def report(region: str):
    """
    Generates and returns a Climate Impact Report PDF for the given region.
    """
    try:
        pdf_bytes = generate_report(region)
    except FileNotFoundError:
        raise HTTPException(404, detail="Required data not found")
    except Exception as e:
        raise HTTPException(500, detail=str(e))

    return StreamingResponse(
        io.BytesIO(pdf_bytes),
        media_type="application/pdf",
        headers={"Content-Disposition": f'attachment; filename="{region}_climate_report.pdf"'},
    )
