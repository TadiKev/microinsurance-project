# backend/users/models.py
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    ROLE_ADMIN = 'admin'
    ROLE_UNDERWRITER = 'underwriter'
    ROLE_AGENT = 'agent'
    ROLE_INVESTIGATOR = 'investigator'
    ROLE_REGULATOR = 'regulator'

    ROLE_CHOICES = (
        (ROLE_ADMIN, 'Admin'),
        (ROLE_UNDERWRITER, 'Underwriter'),
        (ROLE_AGENT, 'Agent'),
        (ROLE_INVESTIGATOR, 'Investigator'),
        (ROLE_REGULATOR, 'Regulator'),
    )

    role = models.CharField(
        max_length=32,
        choices=ROLE_CHOICES,
        default=ROLE_AGENT
    )

    # ✅ Fix reverse accessor clashes by giving unique related_names
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",   # was user_set by default
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_set",   # was user_set by default
        blank=True
    )

    def is_admin(self):
        return self.role == self.ROLE_ADMIN or self.is_superuser

    def __str__(self):
        return f"{self.username} ({self.role})"
