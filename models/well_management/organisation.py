from django.contrib.gis.db import models
from django.contrib.postgres.fields import ArrayField


class Organisation(models.Model):
    """ Organisation
    """

    name = models.CharField(
        max_length=512, unique=True)
    description = models.TextField(null=True, blank=True)

    # this is for ordering
    order = models.PositiveIntegerField(default=0, editable=False,
                                        db_index=True)

    # for the permission
    admins = ArrayField(
        models.IntegerField(), default=list, null=True)
    editors = ArrayField(
        models.IntegerField(), default=list, null=True)
    viewers = ArrayField(
        models.IntegerField(), default=list, null=True)

    class Meta:
        db_table = 'organisation'
        ordering = ['name']

    def __str__(self):
        return self.name

    def is_admin(self, user):
        """ return if admin """
        return user.is_staff or user.id in self.admins
