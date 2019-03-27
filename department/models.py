from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
import mptt


class Department(MPTTModel):

    class Meta():
        verbose_name = 'Department'
        ordering = ('tree_id', 'level')

    name = models.CharField(max_length=250,
                            verbose_name='department name')
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children',
                            verbose_name='PARENT CLASS')

    class MPTTMeta:
        order_insertion_by = ['-name']

    def __str__(self):
        return self.name


mptt.register(Department, order_insertion_by=['-name'])
