from fastapi import APIRouter, HTTPException
from ..schema.model_region import Region
from ..services.avaliable_ec2_instances_types import avaliable_ec2_instances_types

router = APIRouter()

@router.get("/")
async def read_items():
    return {"msg": "Hello World"}

@router.post("/ec2")
async def get_avaliable_ec2_instances_types(region: Region):
    response = avaliable_ec2_instances_types()
    return response