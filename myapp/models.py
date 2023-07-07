from django.db import models
from django.urls import reverse

from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.core.mail import send_mail

from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.template.loader import render_to_string

from django_rest_passwordreset.signals import reset_password_token_created

User = get_user_model()

BLOOD_GROUP_CHOICE = (
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-')
)

CITY_CHOICE = (
    ('lahore', 'lahore'),
    ('Karachi', 'Karachi'),
    ('Faislbad', 'Faislbad')
)

VEHICLE_CHOICES = (
    ('motor_cycle', 'motor_cycle'),
    ('car', 'car'),
    ('jeep', 'jeep'),
    ('mazda', 'mazda'),
    ('truck', 'truck')
)


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    image = models.FileField(upload_to='image/', null=True, blank=True)

    def __str__(self):
        return


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    """
    Handles password reset tokens
    When a token is created, an e-mail needs to be sent to the user
    :param sender: View Class that sent the signal
    :param instance: View Instance that sent the signal
    :param reset_password_token: Token Model Object
    :param args:
    :param kwargs:
    :return:
    """
    # send an e-mail to the user
    context = {
        'current_user': reset_password_token.user,
        'username': reset_password_token.user.username,
        'email': reset_password_token.user.email,
        'reset_password_url': "{}?token={}".format(
            instance.request.build_absolute_uri(reverse('password_reset:reset-password-confirm')),
            reset_password_token.key)
    }

    # render email text
    # email_html_message = render_to_string('email/user_reset_password.html', context)
    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )
    # msg.attach_alternative(email_html_message, "text/html")
    # msg.send()


def validate_cnic(value):
    if '-' in value:
        value = value.replace('-', '')
    if not value.isdigit():
        raise ValidationError('CNIC must contain only digits.')
    if len(value) != 13:
        raise ValidationError('CNIC must be 13 digits long.')


class LisenseData(models.Model):
    name = models.CharField(max_length=100)
    cnic = models.CharField(max_length=14, validators=[validate_cnic])
    phone = models.CharField(max_length=13, null=True, blank=True)
    address = models.CharField(max_length=255)
    lisense_number = models.CharField(max_length=8)
    height = models.CharField(max_length=5, null=True, blank=True)
    blood_group = models.CharField(choices=BLOOD_GROUP_CHOICE, max_length=10, null=True, blank=True)
    city = models.CharField(choices=CITY_CHOICE, max_length=30, null=True, blank=True)
    vehicle_type = models.CharField(choices=VEHICLE_CHOICES, max_length=20)
    issue_date = models.DateField(auto_now_add=True)
    expiry_date = models.DateField()


class TrackDrowsiness(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    count = models.IntegerField(max_length=100, default=0)
    created_at = models.DateTimeField(auto_now_add=True)


def get_or_none(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        return None

