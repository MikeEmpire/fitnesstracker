from functools import wraps
from typing import Dict, Any
from rest_framework import status
from rest_framework.response import Response

def validate_json(schema: Dict[str, Any]):
    """_summary_
    A Decorator that validates the request data against a TypedDict Schema.

    Args:
        schema (Type[Dict[str, Any]]): _description_

    Returns:
        Decorator function that validates the request and returns a 400 error if invalid.
    """

    def decorator(view_func):
        @wraps(view_func)
        def wrapped_view(self, request, *args, **kwargs):
            if not isinstance(request.data, dict):
                return Response(
                    {"error": "Invalid request format. Expected JSON."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            if not hasattr(schema, "__annotations__"):
                raise TypeError(f"{schema} is not a valid TypedDict")

            required_keys = schema.__annotations__.keys()

            missing_keys = [key for key in required_keys if key not in request.data]
            if missing_keys:
                return Response(
                    {"error": f"Missing keys: {', '.join(missing_keys)}"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            return view_func(self, request, *args, **kwargs)

        return wrapped_view

    return decorator
