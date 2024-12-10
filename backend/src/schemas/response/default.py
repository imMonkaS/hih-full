from pydantic import BaseModel


class DefaultResponse(BaseModel):
    status: int
    message: str
    data: list | dict | None | str = None
