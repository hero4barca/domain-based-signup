
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from accounts.models import WhitelistDomains, WhitelistEmails


User = get_user_model()

class SignupViewTest(TestCase):

    def test_signup_with_no_whitlisted_email_or_domain_fails(self):

        signup_form_data = {
            "email": "test@example.com",
            "username": "user01",
            "password1": "password@1",
            "password2": "password@1"
        }
        response = self.client.post(reverse('signup'),
                                     data=signup_form_data, 
                                     follow=True,
                                     content_type='application/x-www-form-urlencoded')
        self.assertEquals(response.status_code, 200 )
        # asser new user not created
        new_user = User.objects.filter(email="test@example.com" ).first()
        self.assertEquals(new_user, None)
