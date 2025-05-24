from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_hello(request):
    """
    A simple view that returns a greeting message.
    """
    return Response({"message": "Hello, world!"})