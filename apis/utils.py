from fastapi import Request, status
from functools import wraps
from jose import jwt
from starlette.responses import RedirectResponse


SECRET_KEY = "it's secret"

def login_required(func):
    @wraps(func)
    async def wrapper(*args, request: Request, **kwargs):
        try:
            _ = get_payload()

        except:
            print("로그인 세션이 만료되었습니다. 다시 로그인하세요.")
            response = RedirectResponse(url="/user/login", status_code=status.HTTP_303_SEE_OTHER)
            response.delete_cookie(key="access-token")
            return response
        
        return func(*args, request, **kwargs)
    return wrapper

def get_payload(request: Request, key=SECRET_KEY):
    token = request.cookies.get("access-token")
    payload = jwt.decode(token, SECRET_KEY)

    return payload
