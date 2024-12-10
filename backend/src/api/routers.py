from fastapi import APIRouter

from api.segmentation import SEGMENTATION_ROUTER
from api.status import STATUS_ROUTER

ROUTER = APIRouter(prefix='/v1')
ROUTER.include_router(STATUS_ROUTER)
ROUTER.include_router(SEGMENTATION_ROUTER)
