from django.test import SimpleTestCase
from django.urls import reverse

profile_url = reverse('profile')
login_url = reverse('login')


class ProfileView(SimpleTestCase):

    def test_profile_page_unauthorized_redirect(self):
        response = self.client.get(profile_url)
        self.assertRedirects(response, login_url + f'?next={profile_url}')
