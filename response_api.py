from fastapi.responses import JSONResponse
from starlette import status as http_status


def make_response(
        message: str = None,
        data: any = None,
        status_code: int = http_status.HTTP_200_OK
):
    response_data = {
        "message": message,
        "data": data
    }

    response_data = {k: v for k, v in response_data.items() if v is not None}

    return JSONResponse(
        status_code=status_code,
        content=response_data
    )
