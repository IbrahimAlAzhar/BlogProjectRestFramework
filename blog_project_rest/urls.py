"""blog_project_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.documentation import include_docs_urls # for documentation purpose(convert schema to documentation)
from rest_framework.schemas import get_schema_view  # schema using for all API endpoints to machine readable document
from rest_framework_swagger.views import get_swagger_view # this red line creates no problem,it works

API_TITLE = 'Blog API'  # we define the 'API_TITLE' and API_DESCRIPTION which one use in schema and documentation
API_DESCRIPTION = 'A Web API for creating and editing blog posts.'
schema_view = get_swagger_view(title=API_TITLE) # use get_swagger_view(3rd party) in place of get_scheme_view(built in)
# use 3rd party app which is 'django-rest-swagger',we have to install it,this pacakge to implement the OpenAPI Specification with a tool called Swagger,this is a third party app,not something with built in support like coreapi,this is the current best practice approach for documenting a RESTful API

# schema_view = get_schema_view(title=API_TITLE)
# schema_view = get_schema_view(title='Blog API') # her we will add a schema to our Blog project and then add two different documentation approaches

# a schema is a machine readable document that outlines all available API endpoints,URLs and the HTTP verbs(GET,POST,PUT,DELETE etc) they support.
# we install Core API(django REST framework has built in support for this) which automatically generate an API schema,Core API is format independent which means it can be used in a wide variety of documentation,after that you decide which document format you want to use it in
# we also install pyyaml which will let us render our schema in the commonly used YAML based OpenAPI format
# Documentation is something added to a scheme that makes it easier for humans to read and consume,when we works with documentation then we should add line in settings.py file
# schema is designed for machines,not humans,to read Django REST Framework also comes with a built-in-API documentation feature that translates schema into a much friendlier format for fellow developers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include('posts.urls')), # if we had multiple apps in a project it might make more sense to create a dedicated api app and then include all other API url routes into it,but for basic projects like this one,we avoid an api app that is just used for routing
    path('api-auth/',include('rest_framework.urls')), # django REST framework has a one line setting to add log in and log out to the browsable API itself,we use 'api-auth' or 'anything-we-want'
    path('api/v1/rest-auth/',include('rest_auth.urls')), # this is 3rd party package for log in,log out,password reset,password reset confirm ,
    path('api/v1/rest-auth/registration/',include('rest_auth.registration.urls')), # if we want to create 'registration' endpoint then we have to define explicitly using rest_auth.registration,,normal rest-auth can't do the registration
    # path('docs/',include_docs_urls(title='Blog API')),  # include 'docs' path with title 'Blog API'
    path('docs/',include_docs_urls(title=API_TITLE,description=API_DESCRIPTION)), # using title which is Blog API and description
    # path('schema/',schema_view), # this schema(machine readable url,http headers) is default in django rest(core api)
    path('swagger-docs/',schema_view), # this schema is 3rd party app(django rest swagger) which is currently best approach for documentation
    # for swagger login and logout we set it to 'rest_framework' login and logout in settings.py file
]
# traditional django and django rest framework does not ship with built in views or urls for user registration(signup).For that reason we need to write our own code from scratch which is a risky approach or we can use django-allauth for sign up process
# third party package django-allauth which comes with user registration as well as social authentication via Facebook,Google,Twitter.On the other hand if we add rest_auth.registration from the django-rest-auth package then we have user registration endpoints too
# it is good practice to always version your APIs-v1/,v2/ etc-since when you make a large change there may be some lag
# time before various consumers of the API can also update. That way you can support a v1 of an API for a period of time
# while also launching a new,updated v2 and avoid breaking other apps that rely on you API back end
# we can use 'api-auth/login' and 'api-auth/logout' for login and logout by using django admin
# we can use 'api/v1/rest-auth/login' for login purpose,we can use 'api/v1/rest-auth/logout' for logout purpose using 'rest_auth.urls'
# we can use 'api/v1/rest-auth/password/reset' for password reset purpose,we can use 'api/v1/rest-auth/password/reset/confirm' for confirming password reset using 'rest_auth.urls'

# we can build this url,if we don't create these url no problem,django automatically works
# we can use 'api/v1/rest-auth/password_change' for changing password ,
# when we enter login then create a token which is store in admin page,and the token is showed as key in the page
# when we logout then the token(key) which one generated after a user login this one will distroy,,logout works on 'rest_framework.urls' path

