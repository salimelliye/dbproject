from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

GENDER_CHOICES = (
    ('MAN','MAN'),
    ('WOMAN','WOMAN'),
    ('OTHER','OTHER'),
)

EMOJI_CHOICES = (
    ('HEART','HEART'),
    ('THUMB','THUMB'),
    ('FIRE','FIRE'),
    ('STAR','STAR')
)

class BaseModel(models.Model):
    id_prefix = '' # To be inherited

    @classmethod
    def generate_id(cls, *args, **kwargs):
        current_year = str(datetime.now().year)[-2:]
        max_id = cls.objects.aggregate(models.Max('id'))['id__max']
        new_id = str(int(max_id[-4:]) + 1).zfill(4) if max_id else '0001'
        return cls.id_prefix + current_year + new_id
    
    def save(self, *args, **kwargs):
        if not getattr(self, self._meta.pk.attname):
            setattr(self, self._meta.pk.attname, self.generate_id())
        super(BaseModel, self).save(*args, **kwargs)
    class Meta:
        abstract = True

class Person(BaseModel):
    id_prefix = "U"
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    person_id = models.CharField(max_length=50, blank=True, primary_key=True)
    gender = models.CharField(max_length=100,choices=GENDER_CHOICES)
    image = models.ImageField(upload_to='person_images/', blank=True)
    dob = models.DateField()

class Friend(BaseModel):
    personID = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='friends')
    friendID = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='user_friends')

class Trip(BaseModel):
    id_prefix = "T"
    tripID = models.AutoField( blank=True, primary_key=True)
    userID = models.ForeignKey(Person, on_delete=models.CASCADE)
    orgID = models.ForeignKey('Organization', on_delete=models.CASCADE)
    plateNb = models.ForeignKey('Vehicle', on_delete=models.CASCADE)
    rideDate = models.DateTimeField() # removed startTime = models.DateTimeField() to avoid repetition
    nbParticipants = models.PositiveIntegerField()
    departure = models.CharField(max_length=255)
    isFeatured = models.BooleanField(default=False)
    isBookmarked = models.BooleanField(default=False)
    participants = models.ManyToManyField('Person', default='', null=True, blank=True, related_name='participants')

class Vehicle(BaseModel):
    plateNb = models.AutoField( blank=True, primary_key=True)
    userID = models.ForeignKey(Person, on_delete=models.CASCADE)
    model = models.CharField(max_length=255)
    make = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    nbSeats = models.PositiveIntegerField()

class Organization(BaseModel):
    id_prefix="O"
    orgID = models.AutoField( blank=True, primary_key=True)
    orgName = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='org_logos/', blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

class Stop(BaseModel):
    id_prefix="S"
    stopID = models.AutoField( blank=True, primary_key=True)
    tripID = models.ForeignKey('Trip', on_delete=models.CASCADE)
    branchID = models.ForeignKey('Branch', on_delete=models.CASCADE)
    location = models.CharField(max_length=500)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    isDestination = models.BooleanField()

class User_Post(BaseModel):
    personID = models.ForeignKey('Person', on_delete=models.CASCADE)
    postID = models.ForeignKey('Post', on_delete=models.CASCADE)

class Branch(BaseModel):
    id_prefix="B"
    branchID = models.AutoField( blank=True, primary_key=True)
    orgID = models.ForeignKey('Organization', on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='branch_images/', blank=True)
    openingHours = models.CharField(max_length=255)

class Post(BaseModel):
    id_prefix="P"
    postID = models.AutoField( blank=True, primary_key=True)
    tripID = models.ForeignKey('Trip', on_delete=models.CASCADE)
    personID = models.ForeignKey('Person', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images/', blank=True)
    description = models.TextField()
    date = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True)
    isBookmarked = models.BooleanField(default=False)

class Reaction(BaseModel):
    postID = models.ForeignKey('Post', on_delete=models.CASCADE)
    commentID = models.ForeignKey('Comment', on_delete=models.CASCADE)
    emojiID = models.ForeignKey('Emoji', on_delete=models.CASCADE)

class Advertisement(BaseModel):
    id_prefix="A"
    adID = models.AutoField( blank=True, primary_key=True)
    postID = models.ForeignKey('Post', on_delete=models.CASCADE)
    duration = models.DateTimeField()
    branchID = models.ForeignKey('Branch', on_delete=models.CASCADE)
    advertiser = models.ForeignKey('Organization', on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    adLink = models.URLField()
    image = models.ImageField(blank=True, upload_to='ad_images/')

class Comment(BaseModel):
    id_prefix="C"
    commentID = models.AutoField( blank=True, primary_key=True)
    postID = models.ForeignKey('Post', on_delete=models.CASCADE)
    personID = models.ForeignKey('Person', on_delete=models.CASCADE)


class Emoji(BaseModel):
    id_prefix="E"
    emojiID = models.AutoField( blank=True, primary_key=True)
    emojiType = models.CharField(max_length=255, choices=EMOJI_CHOICES)
    icon = models.ImageField(upload_to='emoji_icons/')
    commentID = models.ForeignKey('Comment', on_delete=models.CASCADE)
