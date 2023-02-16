
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
                                     data=signup_form_data)
                                     
        self.assertEquals(response.status_code, 200 )
        # asser new user not created
        new_user = User.objects.filter(email="test@example.com" ).first()
        self.assertEquals(new_user, None)


    def test_signup_with_whitelisted_email_successful(self):

        whitelisted_email  = WhitelistEmails.objects.create(
            email = "test@example.com",
            is_active = True
        )
        self.assertIn(whitelisted_email, WhitelistEmails.objects.all())
    
        signup_form_data = {
            "email": "test@example.com",
            "username": "user01",
            "password1": "Password@1",
            "password2": "Password@1"
        }

        response = self.client.post(reverse('signup'),
                                     data=signup_form_data) 
        self.assertEquals(response.status_code, 200 )

        # # asser new user not created
        new_user = User.objects.filter(email="test@example.com" ).first()
        self.assertIsInstance(new_user, User, "New user was not created")

    
    def test_signup_with_whitelisted_domain_successful(self):

        whitelisted_domain  = WhitelistDomains.objects.create(
            domain = "domain.com",
            is_active = True
        )
        self.assertIn(whitelisted_domain, WhitelistDomains.objects.all())
    
        signup_form_data = {
            "email": "test@domain.com",
            "username": "user01",
            "password1": "Password@1",
            "password2": "Password@1"
        }

        response = self.client.post(reverse('signup'),
                                     data=signup_form_data) 
        self.assertEquals(response.status_code, 200 )

        # # asser new user not created
        new_user = User.objects.filter(email="test@domain.com").first()
        self.assertIsInstance(new_user, User, "New user was not created")

    




