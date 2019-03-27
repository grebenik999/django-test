from django.db import models
from django.urls import reverse
from django.db.models import Q
from mptt.models import MPTTModel, TreeForeignKey
import mptt
from datetime import datetime
from department.models import Department


def workers_directory_path(self, filename):
    # file will be uploaded to MEDIA_ROOT/workers_username/<filename>
    return f'workers_{self.username}/{filename}'


class WorkerQuerySet(models.query.QuerySet):

    def search(self, query):
        lookups = (
            Q(department__name__icontains=query) |
            Q(username__icontains=query) |
            Q(position__icontains=query) |
            Q(hire_date__icontains=query) |
            Q(salary__icontains=query))
        return self.filter(lookups).distinct()


class WorkerManager(models.Manager):
    def get_queryset(self):
        return WorkerQuerySet(self.model, using=self.db)

    def features(self):
        return self.get_queryset().featured()

    def search(self, query):
        return self.get_queryset().search(query)


class Worker(models.Model):
    class Meta:
        ordering = ['id']

    department = TreeForeignKey(
        Department, on_delete=models.CASCADE, null=True, blank=True,
        related_name='employee')
    username = models.CharField(max_length=50, blank=True, null=True)
    position = models.CharField(max_length=300, default='co-worker')
    hire_date = models.DateTimeField(auto_now_add=False,
                                     verbose_name='Hire Date',
                                     help_text="Please use the following format: <em>DD/MM/YYYY</em>.")
    salary = models.IntegerField(default=0)
    image = models.ImageField(
        upload_to=workers_directory_path, null=True, blank=True)

    objects = WorkerManager()

    class MPTTMeta:
        order_insertion_by = ['username']

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('details-employee', kwargs={'pk': self.pk})
