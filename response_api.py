from fastapi.responses import JSONResponse
from starlette import status as http_status
from Models import ReturnModel

def make_response(
    status: bool = True,
    message: str = None,
    data: any = None,
    status_code: int = http_status.HTTP_200_OK
):
    return JSONResponse(
        status_code=status_code,
        content=ReturnModel(status=status, message=message, data=data).dict()
    )