from rest_framework import serializers
from users.models import SubscribedUser

class SubscribedUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubscribedUser
        fields = ('name', 'email',)