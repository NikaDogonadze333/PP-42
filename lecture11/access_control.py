from functools import wraps
from typing import Callable, Any, Optional


def require_role(allowed_role: str = "admin") -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Optional[Any]:
            user_role = kwargs.get("user_role")
            if user_role == allowed_role:
                return func(*args, **kwargs)
            else:
                print(f"Permission Denied: User is not an {allowed_role}.")
                return None

        return wrapper

    return decorator