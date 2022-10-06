from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
  """Serializes the path for rclone source and destination"""
  source = serializers.CharField(max_length=255)
  destination = serializers.CharField(max_length=255)
