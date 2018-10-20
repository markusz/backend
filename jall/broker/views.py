from django.http import HttpResponse
from rest_framework import generics
from .serializers import TokenSerializer
from .models import Token


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You are in the root")

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Token.objects.all()
    serializer_class = TokenSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new token."""
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Token.objects.all()
    serializer_class = TokenSerializer