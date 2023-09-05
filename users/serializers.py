from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):

    date_joined = serializers.ReadOnlyField()
    #password = serializers.CharField(write_only=True)
    class Meta(object):

        model = User
        fields = ('id', "username", "can_be_contacted", "can_data_be_shared", "age",
                  'date_joined', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        try:
            user = User.objects.create_user(
                    username=validated_data['username'],
                    can_be_contacted=validated_data['can_be_contacted'],
                    can_data_be_shared=validated_data['can_data_be_shared'],
                    age=validated_data['age'],
                    )
            user.set_password(validated_data['password'])
            user.save()
            return user
        except KeyError:
            raise serializers.ValidationError('a required field is missing')
    
    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        try:
            user.set_password(validated_data['password'])
            user.save()
        except KeyError:
            pass
        return user
    

