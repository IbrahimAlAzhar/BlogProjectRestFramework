from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post


# checking the model creating dummy user and Post which includes post,title and author
class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # create a user
        testuser1 = User.objects.create_user(username='testuser1',password='abc123') # create a simple dummy test user
        testuser1.save()  # save the dummy data,if you don't save the dummy data then no problem
        # create a blog post
        test_post = Post.objects.create(author=testuser1,title='Blog title',body='Body content...')
        test_post.save()  # create a post and save it,if you don't want save it no problem

    def test_blog_content(self):
        post = Post.objects.get(id=1)  # take the item from Post database(only item which id is 1)
        author = f'{post.author}'  # take the author from Post object and save it into post variable
        title = f'{post.title}'  # take the title from Post object using f string and store it into title variable
        body = f'{post.body}'  # take Post object body in body variable using f string
        self.assertEqual(author,'testuser1') # check author(testuser1) with testuser1
        self.assertEqual(title,'Blog title') # here check title of Post which is Blog title check with 'Blog title'
        self.assertEqual(body,'Body content...') # check body is Post.body which contains 'Body content...' check with 'Body content...'





