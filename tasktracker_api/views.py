from rest_framework.decorators import api_view
from rest_framework.response import Response 

@api_view()
def root_route(request):
    return Response({
        "messsage": "Welcome to the Task Tracker API."
    })