import typing

from starlette.requests import Request
from starlette.websockets import WebSocket
from strawberry.permission import BasePermission
from strawberry.types import Info

from fastapi_microsoft_identity import validate_scope, AuthError
    
class IsAdmin(BasePermission):
    message = None

    def has_permission(self, source: typing.Any, info: Info, **kwargs) -> bool:
        request: typing.Union[Request, WebSocket] = info.context["request"]

        if "Authorization" in request.headers:
            has_valid_scope, self.message= authenticate('admin', request)
            return has_valid_scope
        
        return False
    

def authenticate(required_scope, request):
    try:
        validate_scope(required_scope, request)
        return True, 'Success'
    except AuthError as ae:
        return False, ae.error_msg
    except Exception as x:
        return False, str(x)
