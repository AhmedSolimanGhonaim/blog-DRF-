from django.test import TestCase

# Create your tests here.
from .models import Post
from django.contrib.auth.models import User

class BlogTest(TestCase):


    @classmethod

    def setUpTestData(cls):
        test_user1 = User.objects.create_user(username='testuser1', password='12345')
        test_user1.save()


        test_blog = Post.objects.create(
            author=test_user1,
            title='Blog Title',
            body='Blog Content'
        )
        test_blog.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        expected_author = f'{post.author}'
        expected_title = f'{post.title}'
        expected_body = f'{post.body}'
        self.assertEqual(expected_author, 'testuser1')
        self.assertEqual(expected_title, 'Blog Title')
        self.assertEqual(expected_body, 'Blog Content')

        