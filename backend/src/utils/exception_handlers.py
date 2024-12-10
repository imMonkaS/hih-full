from starlette.responses import JSONResponse, Response

from utils.exceptions import (UnknownException)


def unknown_exception_handler(request, exc) -> Response:
    exc = UnknownException()
    return JSONResponse(
        status_code=exc.status_code,
        content={
            'message': exc.msg,
            'error_code': exc.error_code
        },
    )
