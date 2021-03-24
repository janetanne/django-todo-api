# django rest framework
from rest_framework import viewsets

# todo_api
from todo_api.models import ToDo
from todo_api.serializers import ToDoSerializer

# Create your views here.
class ToDoViewSet(viewsets.ModelViewSet):
    """
    This Viewset automatically provides list, create, retrieve, update, partial_update, and destroy actions.
    Inherits from GenericAPIView, which is an extension of REST framework's APIView class.
    """

    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    