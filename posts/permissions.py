# here we want only the author of a specific blog post to be able to edit or delete it,otherwise the blog post should be
# read only.And the superuser account should have full CRUD access to the individual blog instance,but regular user not
'''
class BasePermission(object): # a base class from which all permission classes should inherit
      def has_permission(self,request,view): # return True if permission is granted,False otherwise
          return True

      def has_object_permission(self,request,view,obj): # return True if permission is granted,False otherwise
          return True
'''
from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission): # extends BasePermission, here we want to allow read-only for all requests but for any write requests,such as edit or delete,the author must be the same as the current logged-in user

    def has_object_permission(self, request, view, obj): # we override 'has_object_permission' method
        # read only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS: # if a request contains HTTP verbs included in SAFE_METHODS a tuple containing GET,OPTIONS and HEAD then it is a read only request and permission is granted,if request method is in Safe methods means any logged in user then he can read posts
            return True

        # otherwise the request is for a write of some kind,which means updating the API resource so either create,delete or edit functionality,here we check if the author of the object in question which is our blog post obj.author matches the user making the request 'request.user',
        return obj.author == request.user

