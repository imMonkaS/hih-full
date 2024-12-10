from fastapi import APIRouter

from schemas.response import DefaultResponse

STATUS_ROUTER = APIRouter()


@STATUS_ROUTER.get('/status')
def status():
    return DefaultResponse(
        status=200,
        message='Ping',
        data=None
    )
