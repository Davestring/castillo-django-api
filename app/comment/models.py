"""Comment models module."""

from django.db import models

from ..house.models import HouseModel


class CommentModel(models.Model):
    """CommentModel.

    Extends the Model class from models package and defines the fields for a
    Comment registry.

    Attributes
    ----------
    name : CharField
        User name who wrote the comment.
    lastname : CharField
        User lastname who wrote the comment.
    comment : TextField
        Commet itself.
    active : BooleanField
        True if the comment is active, otherwise False.
    createdAt : DateField
        Date when the comment was created.
    updatedAt : DateField
        Date when the comment was updated.

    """

    name = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    comment = models.TextField(blank=False)
    active = models.BooleanField(default=True)

    house = models.ForeignKey(
        HouseModel, on_delete=models.CASCADE, default=None
    )

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta."""

        db_table = "commet"
