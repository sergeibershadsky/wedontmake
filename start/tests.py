from django.test import SimpleTestCase, override_settings
from django.urls import reverse

profile_url = reverse('profile')
login_url = reverse('login')


@override_settings(DATABASE={'default': dict(ENGINE='django.db.backends.sqlite3', NAME=':memory:')})
class ProfileView(SimpleTestCase):

    def test_profile_page_unauthorized_redirect(self):
        response = self.client.get(profile_url)
        self.assertRedirects(response, login_url + f'?next={profile_url}')
