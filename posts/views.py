from django.shortcuts import render
from rest_framework import generics,permissions,viewsets
from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer,UserSerializer
from django.contrib.auth import get_user_model


# ListAPIView is using for read only endpoint collections(like as listview),
# RetriveAPIView for a read only single endpoint which is same as detail view in traditional django
# ListCreateAPIView which is use for read and write(create)
# RetriveUpdateDestroyAPIView which is use for read,update,deleted,,RetrivieUpdateView is use for read and update,,
# RetriveDeleteView is using for read and delete

'''
class PostList(generics.ListCreateAPIView): # this one inherits from ListCreateAPIView where using for List view and create view
    # permission_classes = (permissions.IsAuthenticated,) # we set the permission in settings.py file, add permissions for logged in user can see the ListView,only logged in users can view our API,if a user is superuser or any other user he can access ListView,DetailView
    queryset = Post.objects.all()
    serializer_class = PostSerializer # using PostSerializer(serializer converts the raw data to JSON format)


class PostDetail(generics.RetrieveUpdateDestroyAPIView): # this one inherits from a api view where you can see detail,update,delete of a post
    # permission_classes = (permissions.IsAuthenticated,) # we set the permissions in settings.py file, if a user is logged in then he can see the detailview
    permission_classes = (IsAuthorOrReadOnly,)  # here use the permission is Author can update or delete his post and rest of author just read the post(permission works on permission.py file,where override django build in permission class)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
'''

# A good rule of thumb is to start with views and urls,as your API grows in complexity if you find yourself repeating the same endpoint patterns over and over again,then use viewsets and routers
# we use PostViewSet(ViewSet) in place of PostList and PostDetail,it is viewset which combine the logic for multiple related views into a single class,one viewset can replace multiple views
class PostViewSet(viewsets.ModelViewSet): # inherit from ModelViewSet which provides both a list view and detail view,and we no longer have to repeat the same queryset and serializer_class for each list view and detail view as we did previously
    permission_classes = (IsAuthorOrReadOnly,) # this permission_classes define the author can update or delete,and other user just can read
    queryset = Post.objects.all() # take all post and store it to queryset variable
    serializer_class = PostSerializer # using PostSerializer(serializer converts raw data to JSON format)


# using UserViewSet in place of UserList and UserDetail,in UserList and UseDetailView there are some repeat of code for that reason we create one viewset
class UserViewSet(viewsets.ModelViewSet):  # we don't need to use permission_classes in UserViewSet,so any one user can update the username
    queryset = get_user_model().objects.all()  # take all objects
    serializer_class = UserSerializer  # using serializer class
'''
class UserList(generics.ListCreateAPIView): # inherits from ListCreateAPIView which is using for List view and create
    queryset = get_user_model().objects.all()  # take all attributes from get_user_model which is build in from django
    serializer_class = UserSerializer # using UserSerializer(serializer converts the raw data into JSON format)


class UserDetail(generics.RetrieveUpdateDestroyAPIView): # inherits from RetrieveUpdateDestroyAPIView where a user can see detail,update or delete,
    # here we don't use 'permission_classes like IsAuthorOrReadOnly',if we set this then only the author can see detail,update or delete and other user just see the detail
    queryset = get_user_model().objects.all() # takes all attributes from user_model(build in) like id,username etc
    serializer_class = UserSerializer
'''