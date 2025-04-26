# backend/models/vessel.py

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class Vessel(BaseModel):
    mmsi: int                 = Field(..., alias="MMSI")
    timestamp: datetime       = Field(..., alias="BaseDateTime")
    lat: float                = Field(..., alias="LAT")
    lon: float                = Field(..., alias="LON")
    sog: Optional[float]      = Field(None, alias="SOG")
    cog: Optional[float]      = Field(None, alias="COG")
    heading: Optional[float]  = Field(None, alias="Heading")
    vessel_name: Optional[str]= Field(None, alias="VesselName")
    imo: Optional[str]        = Field(None, alias="IMO")
    callsign: Optional[str]   = Field(None, alias="CallSign")
    vessel_type: Optional[int]= Field(None, alias="VesselType")
    status: Optional[int]     = Field(None, alias="Status")
    length: Optional[float]   = Field(None, alias="Length")
    width: Optional[float]    = Field(None, alias="Width")
    draft: Optional[float]    = Field(None, alias="Draft")
    cargo: Optional[str]      = Field(None, alias="Cargo")
    transceiver_class: Optional[str] = Field(None, alias="TransceiverClass")

    class Config:
        allow_population_by_field_name = True