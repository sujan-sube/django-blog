from django.test import TestCase
from django.core.urlresolvers import reverse
from blog.models import Post

class BlogTest(TestCase):

    def create_post(self):
        Post.objects.create(title="Test Post", text="This is a test description", author=1)

    def test_blog_post_list(self):
        url = reverse("post_list")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

    def test_blog_login(self):
        url = reverse("login")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

    def test_post_edit(self):
        url = reverse("post_edit", kwargs={'pk': 1})
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
