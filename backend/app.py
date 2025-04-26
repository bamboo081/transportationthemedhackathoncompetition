from fastapi import FastAPI
from backend.routes.simulation import router as sim_router
from backend.routes.report import router as report_router
from dotenv import load_dotenv
load_dotenv()

app = FastAPI(title="LogMap 3.0 API", version="1.0")

# Route for the root URL "/"
@app.get("/")
def read_root():
    return {"message": "Welcome to the LogMap 3.0 API!"}

# Mount our two route groups
app.include_router(sim_router, prefix="", tags=["simulation"])
app.include_router(report_router, prefix="", tags=["report"])