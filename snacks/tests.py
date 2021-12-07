from django.test import SimpleTestCase
from django.urls import reverse

class HomeTests(SimpleTestCase):
    def test_home_page_template(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "home.html")

    def test_home_page_code(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class AboutUsTests(SimpleTestCase):
    def test_abouts_page_template(self):
        url = reverse("about_us")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "about_us.html")

    def test_aboutus_page_code(self):
        url = reverse("about_us")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)