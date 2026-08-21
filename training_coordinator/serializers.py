from rest_framework import serializers
from .models import TrainingCoordinator

class TrainingCoordinatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingCoordinator
        fields = '__all__'
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }