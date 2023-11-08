from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

GENDER_CHOICES = (
    ('MAN','MAN'),
    ('WOMAN','WOMAN'),
    ('OTHER','OTHER'),
)

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    person_id = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=100,choices=GENDER_CHOICES)
    image = models.ImageField(blank=True)
    dob = models.DateField()

    def save(self, *args, **kwargs):
        if not self.person_id:
            # Get the last two digits of the current year
            current_year = str(datetime.now().year)[-2:]
            # Find the maximum project ID in the database and increment it
            max_id = Person.objects.aggregate(models.Max('person_id'))['person_id__max']
            new_id = str(int(max_id[-4:]) + 1).zfill(4) if max_id else '0001'  # If no existing records, start with '0001'
            self.person_id = 'P' + current_year + new_id  # Add 'p' prefix
        super(Person, self).save(*args, **kwargs)
    