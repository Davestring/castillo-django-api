"""User models module."""
from typing import List

from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, DateTimeField, EmailField

from app.user.managers import UserManager


class User(AbstractUser):
    """Extends the `AbstractUser` class from `django.contrib.auth.models` and defines the fields for an User registry.

    Attributes
    ----------
    created : DateTimeField
        Date when the user registry was created.
    date_joined : None
        Overwrite existing `date_joined` field so we can use `created` as our creation date.
    email : EmailField
        User email, this field should be unique and the `USERNAME_FIELD`.
    first_name : None
        Overwrite the `first_name` in order to avoid using this attribute.
    first_surname : CharField
        User's first surname.
    last_login : None
        Overwrite the `last_login` in order to avoid using this attribute.
    last_name : None
        Overwrite the `last_name` in order to avoid using this attribute.
    last_surname : CharField
        User's last surname.
    name : CharField
        User's name and middle name.
    objects : UserManager
        User database manager.
    REQUIRED_FIELDS : List[str]
        Overwrite existing REQUIRED_FIELDS field.
    updated : DateTimeField
        Date when the user registry was updated.
    username : None
        Overwrite existing username so we can enable `email` as our identifier.
    USERNAME_FIELD : str
        Model field to be the new identifier handled by Django.

    """

    date_joined = None
    email = EmailField(unique=True, max_length=255)
    first_name = None
    last_login = None
    last_name = None
    username = None

    name = CharField(blank=True, default=None, max_length=150, null=True)
    first_surname = CharField(blank=True, default=None, max_length=150, null=True)
    last_surname = CharField(blank=True, default=None, max_length=150, null=True)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    objects = UserManager()

    REQUIRED_FIELDS: List[str] = []
    USERNAME_FIELD = "email"

    class Meta:
        """Meta.

        Model meta options.

        Attributes
        ----------
        db_table : str

        """

        db_table = "user"
