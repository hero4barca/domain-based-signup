from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)


class WhitelistDomains(models.Model):

    class Meta:
        verbose_name = _("Whitelisted Domain")
        verbose_name_plural = _("Whitelisted Domains")

    domain = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    # denotes the day the domain was created
    created_on = models.DateTimeField(
                                    auto_now_add=True
                                )
    # denotes last update
    updated_on = models.DateTimeField(
        auto_now=True
    )


class WhitelistEmails(models.Model):

    class Meta:
        verbose_name = _("Whitelisted Email")
        verbose_name_plural = _("Whitelisted Emails")

    email = models.EmailField(null=False)
    is_active = models.BooleanField(default=True)

    # denotes the day the email record was created
    created_on = models.DateTimeField(
                                    auto_now_add=True
                                )
    # denotes last update
    updated_on = models.DateTimeField(
        auto_now=True
    )
