# the serializer not only transforms data into JSON,it can also specify which fields to include or exclude.In our case
# we will include the id field Django automatically adds to database models but we will exclude the updated_at field by not including it int our fields
from rest_framework import serializers
from .models import Post
from django.contrib.auth import get_user_model


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','author','title','body','created_at') # here define this fields we only use for convert data to JSON format
        model = Post  # the database model will have far more fields than what needs to be exposed,Django REST framework's powerful serializer class makes it extremely straightforward to control this


# traditional django has a built in User model class,so we do not need database model.so create just serializer,views and url routes
class UserSerializer(serializers.ModelSerializer):  # inherits from ModelSerializer

    class Meta:
        model = get_user_model() # get_user_model is django build in for User,we just using id,username field,by using get_user_model we ensure that we are referring to the correct user model
        fields = ('id','username')
