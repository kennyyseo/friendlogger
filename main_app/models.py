from django.db import models
from django.urls import reverse

# Create your models here.

EVENTS = (
    ('H', 'Hangout'),
    ('M', 'Meal'),
    ('S', 'Special Occassion'),
)


class Memory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    year = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('memories_detail', kwargs={'pk': self.id})


class Friend(models.Model):
    name = models.CharField(max_length=100)
    ethnicity = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    age = models.IntegerField()
    memories = models.ManyToManyField(Memory)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'friend_id': self.id})


class Meeting(models.Model):
    date = models.DateField('Meeting Date')
    event = models.CharField(
        max_length=1,
        choices=EVENTS,
        default=EVENTS[0][0]
    )

    friend = models.ForeignKey(Friend, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_event_display()} on {self.date}"

    class Meta:
        ordering = ['-date']
