"""Insight models module."""

from django.db import models


class InsightModel(models.Model):
    """InsightModel.

    Extends the Model class from models package and defines the fields for a
    Insight registry.

    Attributes
    ----------
    title : CharField
        Insight title.
    caption : CharField
        Insight optional caption text.
    summary : TextField
        Insight description.
    cover : TextField
        Insight base64 image.
    created : DateField
        Date when the service was created.
    updated : DateField
        Date when the services was updated.

    """

    title = models.CharField(max_length=255)

    caption = models.CharField(max_length=255, default=None)

    summary = models.TextField()

    cover = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """__str__.

        Object representation in string format.

        """
        return self.title

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

        db_table = "insight"

        verbose_name = "Insight"

        verbose_name_plural = "Insights"
