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
    created : DateField
        Date when the comment was created.
    updated : DateField
        Date when the comment was updated.

    """

    name = models.CharField(max_length=64)

    lastname = models.CharField(max_length=64)

    comment = models.TextField(blank=False)

    active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    house = models.ForeignKey(
        HouseModel,
        default=None,
        on_delete=models.CASCADE,
        related_name="comments",
    )

    class Meta:
        """Meta.

        Model meta options.

        Attributes
        ----------
        db_table : str
            The name of the database table to use for the model.
        verbose_name : str
            Custom model name.
        verbose_name_plural : str
            Custom model plural name.

        """

        db_table = "commet"

        verbose_name = "Comment"

        verbose_name_plural = "Comments"
