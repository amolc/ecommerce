from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager
)

from organisations.models import (
    Organisation
)


class StaffManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **kwargs):
        kwargs.setdefault('is_super_admin', True)
        kwargs.setdefault('is_admin', True)

        user = self.create_user(
            agency_id=1,
            email=email,
            password=password,
            **kwargs
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class Staff(AbstractBaseUser):
    objects: StaffManager = StaffManager()  # type: ignore
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']

    id: models.AutoField = models.AutoField(
        primary_key=True,
    )
    email: models.EmailField = models.EmailField(
        null=True,
        blank=True,
    )
    password: models.CharField = models.CharField(
        max_length=100
    )
    first_name: models.CharField = models.CharField(
        max_length=200
    )
    last_name: models.CharField = models.CharField(
        max_length=200
    )
    mobile_number: models.CharField = models.CharField(
        max_length=15,
        null=True,
        blank=True
    )
    city: models.CharField = models.CharField(
        max_length=200
    )
    total_sales: models.DecimalField = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        null=True,
        blank=True
    )
    hire_date: models.DateField = models.DateField(
        null=True,
        blank=True
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
    is_agent: models.BooleanField = models.BooleanField(
        default=True
    )
    created_at: models.DateTimeField = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at: models.DateTimeField = models.DateTimeField(
        auto_now=True,
    )

    organisation: models.ForeignKey = models.ForeignKey(
        Organisation,
        on_delete=models.DO_NOTHING,
        related_name="staff",
    )


class StaffLog(models.Model):
    logid: models.BigAutoField = models.BigAutoField(
        primary_key=True,
        editable=False
    )
    transaction_name: models.CharField = models.CharField(
        max_length=500
    )
    mode: models.CharField = models.CharField(
        max_length=100
    )
    log_message: models.TextField = models.TextField()
    admin: models.ForeignKey = models.ForeignKey(
        "Staff",
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
        related_name="log_admin_id",
    )
    is_app: models.BooleanField = models.BooleanField(
        default=False
    )
    log_date: models.DateTimeField = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.transaction_name
