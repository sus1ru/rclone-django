from os import stat
from urllib import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rclone_api import serializers


class HelloApiView(APIView):
  """Test API View"""
  serializer_class = serializers.HelloSerializer

  def get(self, request, format=None):
    """Returns a list of APIView features"""
    an_apiview = ['apple', 'oranges', 'grapes', 'banana']

    return Response({'message': 'Hello!', 'an_apiview': an_apiview})

  def post(self, request):
    """Create a rclone command"""
    serializer = self.serializer_class(data=request.data)

    if serializer.is_valid():
      spath = serializer.validated_data.get('source')
      dpath = serializer.validated_data.get('destination')
      rclone_command = f'rclone copy "{spath}" "{dpath}"'
      return Response({'rclone_command': rclone_command})
    else:
      return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST,
      )
  
  def put(self, request, pk=None):
    """Handle updating an oject"""
    return Response({'method': 'PUT'})

  def patch(self, request, pk=None):
    """Handle a partial update of an oject"""
    return Response({'method': 'PATCH'})

  def patch(self, request, pk=None):
    """Delte an oject"""
    return Response({'method': 'DELETE'})
