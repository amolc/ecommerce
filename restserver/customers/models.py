from typing import (
    Any,
)

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager
)

from organisations.models import (
    Organisation
)


class CustomerManager(BaseUserManager):
    def create_user(self, mobile_number: str, password: str|None=None, **kwargs: Any):
        user = self.model(mobile_number=mobile_number, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        
        return user

    def create_superuser(self, email: str, password: str, **kwargs: Any):
        kwargs.setdefault('is_super_admin', True)
        kwargs.setdefault('is_admin', True)

        user = self.create_user(
            org_id=1,
            email=email,
            password=password,
            **kwargs
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class Customer(AbstractBaseUser):
    objects: CustomerManager = CustomerManager()  # type: ignore
    USERNAME_FIELD = 'mobile_number'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    id: models.AutoField = models.AutoField(
        primary_key=True,
    )
    email: models.EmailField = models.EmailField(
        null=True,
        blank=True,
    )
    password: models.CharField = models.CharField(
        max_length=100,
    )
    first_name: models.CharField = models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )
    last_name: models.CharField = models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )
    city: models.CharField = models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )
    mobile_number: models.CharField = models.CharField(
        max_length=15,
        unique=True,
    )
    billing_address: models.TextField = models.TextField(
        null=True,
        blank=True,
    )
    billing_address_specifier: models.TextField = models.TextField(
        blank=True,
        null=True
    )
    billing_address2: models.TextField = models.TextField(
        blank=True,
        null=True
    )
    billing_address2_specifier: models.TextField = models.TextField(
        blank=True,
        null=True
    )
    country: models.CharField = models.CharField(
        max_length=120,
        null=True,
        blank=True,
    )
    state: models.CharField = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )
    postal_code: models.CharField = models.CharField(
        max_length=10,
        null=True,
        blank=True,
    )
    is_active: models.BooleanField = models.BooleanField(
        default=True
    )
    is_super_admin: models.BooleanField = models.BooleanField(
        default=False
    )
    is_admin: models.BooleanField = models.BooleanField(
        default=False
    )
    is_customer: models.BooleanField = models.BooleanField(
        default=False
    )
    is_staff: models.BooleanField = models.BooleanField(
        default=False
    )
    created_at: models.DateTimeField = models.DateTimeField(
        auto_now_add=True
    )
    updated_at: models.DateTimeField = models.DateTimeField(
        auto_now=True
    )

    organisation: models.ForeignKey = models.ForeignKey(
        Organisation,
        on_delete=models.DO_NOTHING,
        related_name="customers",
    )
    
    def __str__(self):
        return (
            f"{self.first_name} {self.last_name}"
        )


class CustomerLog(models.Model):
    id: models.BigAutoField = models.BigAutoField(
        primary_key=True,
    )
    transaction_name: models.CharField = models.CharField(
        max_length=500
    )
    mode: models.CharField = models.CharField(
        max_length=100
    )
    log_message: models.TextField = models.TextField()
    user: models.ForeignKey = models.ForeignKey(
        "Customer",
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
        related_name="log_Customer_id",
    )
    is_app: models.BooleanField = models.BooleanField(
        default=False
    )
    log_date: models.DateTimeField = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.transaction_name
    
