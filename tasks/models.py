from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=500, blank=True)

    def save(self, *args, **kwargs):
        already_present_slugs = Project.objects.filter(slug = self.slug)
        new_slug = f"{'-'.join(self.name.split(' '))}-{already_present_slugs.count()}"
        self.slug = new_slug
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    dateTimeOfCreation = models.DateTimeField(auto_now=True)
    is_task_started = models.BooleanField(default=False)
    date_time_of_task_starting = models.DateTimeField(null=True, blank=True)
    date_time_of_task_ending = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.dateTimeOfCreation}'
