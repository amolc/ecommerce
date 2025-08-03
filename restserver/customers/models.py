from typing import Any

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from organisations.models import Organisation


class CustomerManager(BaseUserManager):
    def create_user(self, mobile_number: str, email: str, password: str | None = None, **kwargs: Any):
        if not mobile_number:
            raise ValueError("The mobile number is required.")
        if not email:
            raise ValueError("The email address is required.")

        email = self.normalize_email(email)
        user = self.model(
            mobile_number=mobile_number,
            email=email,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, mobile_number: str, email: str, password: str, **kwargs: Any):
        from organisations.models import Organisation

        kwargs.setdefault('is_super_admin', True)
        kwargs.setdefault('is_admin', True)
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)

        # Try to get Organisation with ID=1
        try:
            organisation = Organisation.objects.get(id=1)
        except Organisation.DoesNotExist:
            raise ValueError("Organisation with ID=1 does not exist. Create it first.")

        kwargs['organisation'] = organisation

        return self.create_user(
            mobile_number=mobile_number,
            email=email,
            password=password,
            **kwargs
        )



class Customer(AbstractBaseUser, PermissionsMixin):
    objects = CustomerManager()

    USERNAME_FIELD = 'mobile_number'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    id = models.AutoField(primary_key=True)
    email = models.EmailField(null=True, blank=True)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    mobile_number = models.CharField(max_length=15, unique=True)
    billing_address = models.TextField(null=True, blank=True)
    billing_address_specifier = models.TextField(blank=True, null=True)
    billing_address2 = models.TextField(blank=True, null=True)
    billing_address2_specifier = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=120, null=True, blank=True)
    state = models.CharField(max_length=250, null=True, blank=True)
    postal_code = models.CharField(max_length=10, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_super_admin = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)  # Required by Django admin

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    organisation = models.ForeignKey(
        Organisation,
        on_delete=models.DO_NOTHING,
        related_name="customers"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class CustomerLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    transaction_name = models.CharField(max_length=500)
    mode = models.CharField(max_length=100)
    log_message = models.TextField()
    user = models.ForeignKey(
        Customer,
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
        related_name="log_Customer_id",
    )
    is_app = models.BooleanField(default=False)
    log_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.transaction_name
