from django.urls import path
from rest_framework.routers import SimpleRouter
# from .views import PostList, PostDetail, UserList, UserDetail
from .views import UserViewSet, PostViewSet
# we'll use SimpleRouter but it's also possible to create custom routers for more advanced functionality


router = SimpleRouter() # using router for url,we use one router 'users' for UserList and UserDetail view and another router '' for Postlist and Postdetail view
router.register('users',UserViewSet, base_name='users')  # '/users' for user list and '/users/1' for user detail (here 1 is pk),the router is set to SimpleRouter and we "register" each viewset for Users and Posts
router.register('',PostViewSet, base_name='posts')  # '/' url for post list and ''/1 is for post detail (here 1 is pk)
urlpatterns = router.urls  # we set our urls to use the new router and set it to urlpatterns

'''
urlpatterns = [
    path('users/',UserList.as_view()), # for show the list of all of user
    path('users/<int:pk>/',UserDetail.as_view()), # for see the detailview of a user,when we used class based detail view we need a pk which provides by django automatically
    path('', PostList.as_view()),  # there no need use 'name' because we are not using template in here
    path('<int:pk>/',PostDetail.as_view()), # for DetailView django needs pk
]
'''