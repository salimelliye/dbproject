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



class Person(models.Model):
    id_prefix = 'P'
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    personID = models.CharField(max_length=50, blank=True, primary_key=True)
    gender = models.CharField(max_length=100,choices=GENDER_CHOICES)
    image = models.ImageField(upload_to='person_images/', blank=True)
    dob = models.DateField()
    def save(self, *args, **kwargs):
        if not self.personID:
            current_year = str(datetime.now().year)[-2:]
            max_id = Person.objects.aggregate(models.Max('personID'))['personID__max']
            new_id = str(int(max_id[-4:]) + 1).zfill(4) if max_id else '0001'  
            self.personID = self.id_prefix + current_year + new_id  
        super(Person, self).save(*args, **kwargs)

class Friend(models.Model):
    personID = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='friends')
    friendID = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='user_friends')

class Trip(models.Model):
    id_prefix = "T"
    name = models.CharField(max_length=200, null=True)
    tripID = models.CharField(max_length=500, blank=True, primary_key=True)
    userID = models.ForeignKey(Person, on_delete=models.CASCADE)
    orgID = models.ForeignKey('Organization', on_delete=models.CASCADE, blank=True, null=True)
    plateNb = models.ForeignKey('Vehicle', on_delete=models.CASCADE)
    rideDate = models.DateTimeField() 
    description = models.TextField(null=True)
    nbParticipants = models.PositiveIntegerField()
    departure = models.CharField(max_length=255)
    isCompleted = models.BooleanField(default=False)
    isFeatured = models.BooleanField(default=False)
    isBookmarked = models.BooleanField(default=False)
    participants = models.ManyToManyField('Person', default='', null=True, blank=True, related_name='participants')
    def save(self, *args, **kwargs):
        if not self.tripID:
            current_year = str(datetime.now().year)[-2:]
            max_id = Trip.objects.aggregate(models.Max('tripID'))['tripID__max']
            new_id = str(int(max_id[-4:]) + 1).zfill(4) if max_id else '0001'  
            self.tripID = self.id_prefix + current_year + new_id  
        super(Trip, self).save(*args, **kwargs)


class Vehicle(models.Model):
    plateNb = models.AutoField( blank=True, primary_key=True)
    userID = models.ForeignKey(Person, on_delete=models.CASCADE)
    model = models.CharField(max_length=255)
    make = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    nbSeats = models.PositiveIntegerField()

class Organization(models.Model):
    id_prefix="O"
    orgID = models.CharField(max_length=10, unique=True, primary_key=True, blank=True)
    orgName = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='org_logos/', blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.orgID:
            current_year = str(datetime.now().year)[-2:]
            max_id = Organization.objects.aggregate(models.Max('orgID'))['orgID__max']
            new_id = str(int(max_id[-4:]) + 1).zfill(4) if max_id else '0001'  
            self.orgID = self.id_prefix + current_year + new_id  
        super(Organization, self).save(*args, **kwargs)

class Stop(models.Model):
    id_prefix="S"
    stopID = models.AutoField( blank=True, primary_key=True)
    tripID = models.ForeignKey('Trip', on_delete=models.CASCADE)
    branchID = models.ForeignKey('Branch', on_delete=models.CASCADE)
    location = models.CharField(max_length=500)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    isDestination = models.BooleanField()

    def save(self, *args, **kwargs):
        if not self.stopID:
            current_year = str(datetime.now().year)[-2:]
            max_id = Stop.objects.aggregate(models.Max('stopID'))['stopID__max']
            new_id = str(int(max_id[-4:]) + 1).zfill(4) if max_id else '0001'  
            self.stopID = self.id_prefix + current_year + new_id  
        super(Stop, self).save(*args, **kwargs)

class User_Post(models.Model):
    personID = models.ForeignKey('Person', on_delete=models.CASCADE)
    postID = models.ForeignKey('Post', on_delete=models.CASCADE)

class Branch(models.Model):
    id_prefix="B"
    branchID = models.AutoField( blank=True, primary_key=True)
    orgID = models.ForeignKey('Organization', on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='branch_images/', blank=True)
    openingHours = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.branchID:
            current_year = str(datetime.now().year)[-2:]
            max_id = Branch.objects.aggregate(models.Max('branchID'))['branchID__max']
            new_id = str(int(max_id[-4:]) + 1).zfill(4) if max_id else '0001'  
            self.branchID = self.id_prefix + current_year + new_id  
        super(Branch, self).save(*args, **kwargs)

class Post(models.Model):
    id_prefix="P"
    postID = models.AutoField( blank=True, primary_key=True)
    tripID = models.ForeignKey('Trip', on_delete=models.CASCADE)
    personID = models.ForeignKey('Person', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images/', blank=True)
    description = models.TextField()
    date = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True)
    isBookmarked = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.postID:
            current_year = str(datetime.now().year)[-2:]
            max_id = Post.objects.aggregate(models.Max('postID'))['postID__max']
            new_id = str(int(max_id[-4:]) + 1).zfill(4) if max_id else '0001'  
            self.postID = self.id_prefix + current_year + new_id  
        super(Post, self).save(*args, **kwargs)

class Reaction(models.Model):
    postID = models.ForeignKey('Post', on_delete=models.CASCADE)
    commentID = models.ForeignKey('Comment', on_delete=models.CASCADE)
    emojiID = models.ForeignKey('Emoji', on_delete=models.CASCADE)

class Advertisement(models.Model):
    id_prefix="A"
    adID = models.AutoField( blank=True, primary_key=True)
    postID = models.ForeignKey('Post', on_delete=models.CASCADE)
    duration = models.DateTimeField()
    branchID = models.ForeignKey('Branch', on_delete=models.CASCADE)
    advertiser = models.ForeignKey('Organization', on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    adLink = models.URLField()
    image = models.ImageField(blank=True, upload_to='ad_images/')

    def save(self, *args, **kwargs):
        if not self.adID:
            current_year = str(datetime.now().year)[-2:]
            max_id = Advertisement.objects.aggregate(models.Max('adID'))['adID__max']
            new_id = str(int(max_id[-4:]) + 1).zfill(4) if max_id else '0001'  
            self.adID = self.id_prefix + current_year + new_id  
        super(Advertisement, self).save(*args, **kwargs)

class Comment(models.Model):
    id_prefix="C"
    commentID = models.AutoField( blank=True, primary_key=True)
    postID = models.ForeignKey('Post', on_delete=models.CASCADE)
    personID = models.ForeignKey('Person', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.commentID:
            current_year = str(datetime.now().year)[-2:]
            max_id = Comment.objects.aggregate(models.Max('commentID'))['commentID__max']
            new_id = str(int(max_id[-4:]) + 1).zfill(4) if max_id else '0001'  
            self.commentID = self.id_prefix + current_year + new_id  
        super(Comment, self).save(*args, **kwargs)


class Emoji(models.Model):
    id_prefix="E"
    emojiID = models.AutoField( blank=True, primary_key=True)
    emojiType = models.CharField(max_length=255, choices=EMOJI_CHOICES)
    icon = models.ImageField(upload_to='emoji_icons/')
    commentID = models.ForeignKey('Comment', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.emojiID:
            current_year = str(datetime.now().year)[-2:]
            max_id = Emoji.objects.aggregate(models.Max('emojiID'))['emojiID__max']
            new_id = str(int(max_id[-4:]) + 1).zfill(4) if max_id else '0001'  
            self.emojiID = self.id_prefix + current_year + new_id  
        super(Emoji, self).save(*args, **kwargs)
