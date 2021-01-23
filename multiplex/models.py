import datetime

from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic/CustomerProfilePic/', null=True, blank=True)
    mobile = models.CharField(max_length=20, null=False)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_instance(self):
        return self

    def __str__(self):
        return self.user.first_name


CHOICES = (
    ('Older_Kids', 'Older Kids (7+)'),
    ('Teens', 'Teens (13+)'),
    ('Young_Adults', 'Young Adults (16+)'),
    ('Adults', 'Adults (18+)'),
)
Category_CHOICES = (
    ('Action', 'action'),
    ('Comedy', 'comedy'),
    ('Drama', 'drama'),
    ('Fantasy', 'fantasy'),
    ('Horror', 'horror'),
    ('Mystery', 'mystery'),
    ('Romance', 'romance'),
)
Hall_CHOICES = (
    ('A', 'a'),
    ('B', 'b'),
    ('C', 'c'),
    ('D', 'd'),
)


class Movie(models.Model):
    name = models.CharField(max_length=50, null=True)
    actor = models.CharField(max_length=50, null=True)
    director = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=500, null=True)
    poster = models.ImageField(upload_to='movie_pic/movie_poster/', null=True, blank=True)
    video = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, choices=Category_CHOICES, default="General")
    release_date = models.DateField(default=datetime.date.today)
    price = models.IntegerField(default=100)
    org_price = models.IntegerField(default=price)
    popularity = models.IntegerField(default=0)
    out_date = models.DateField(default=datetime.date.today)
    limitation = models.CharField(max_length=30, choices=CHOICES, default='Older Kids (7+)')
    hall = models.CharField(max_length=10, choices=Hall_CHOICES, default='A')
    def __str__(self):
        return self.name


class Feedback(models.Model):
    date = models.DateField(auto_now=True)
    by = models.CharField(max_length=40)
    message = models.CharField(max_length=500)


class Booking(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    date = models.DateField()
    seatNumber = models.CharField(max_length=500)
    totalSeat = models.PositiveIntegerField()
    cost = models.PositiveIntegerField()
    watchers = models.CharField(max_length=500, null=True)
    bookingDate = models.DateField(auto_now=True)

    def __str__(self):
        return self.customer


class Seat(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, null=True)
    date = models.DateField()
    A1 = models.BooleanField(default=True)
    A2 = models.BooleanField(default=True)
    A3 = models.BooleanField(default=True)
    A4 = models.BooleanField(default=True)
    A5 = models.BooleanField(default=True)
    A6 = models.BooleanField(default=True)
    A7 = models.BooleanField(default=True)
    A8 = models.BooleanField(default=True)
    A9 = models.BooleanField(default=True)
    A10 = models.BooleanField(default=True)
    A11 = models.BooleanField(default=True)
    A12 = models.BooleanField(default=True)
    B1 = models.BooleanField(default=True)
    B2 = models.BooleanField(default=True)
    B3 = models.BooleanField(default=True)
    B4 = models.BooleanField(default=True)
    B5 = models.BooleanField(default=True)
    B6 = models.BooleanField(default=True)
    B7 = models.BooleanField(default=True)
    B8 = models.BooleanField(default=True)
    B9 = models.BooleanField(default=True)
    B10 = models.BooleanField(default=True)
    B11 = models.BooleanField(default=True)
    B12 = models.BooleanField(default=True)
    C1 = models.BooleanField(default=True)
    C2 = models.BooleanField(default=True)
    C3 = models.BooleanField(default=True)
    C4 = models.BooleanField(default=True)
    C5 = models.BooleanField(default=True)
    C6 = models.BooleanField(default=True)
    C7 = models.BooleanField(default=True)
    C8 = models.BooleanField(default=True)
    C9 = models.BooleanField(default=True)
    C10 = models.BooleanField(default=True)
    C11 = models.BooleanField(default=True)
    C12 = models.BooleanField(default=True)
    D1 = models.BooleanField(default=True)
    D2 = models.BooleanField(default=True)
    D3 = models.BooleanField(default=True)
    D4 = models.BooleanField(default=True)
    D5 = models.BooleanField(default=True)
    D6 = models.BooleanField(default=True)
    D7 = models.BooleanField(default=True)
    D8 = models.BooleanField(default=True)
    D9 = models.BooleanField(default=True)
    D10 = models.BooleanField(default=True)
    D11 = models.BooleanField(default=True)
    D12 = models.BooleanField(default=True)
    E1 = models.BooleanField(default=True)
    E2 = models.BooleanField(default=True)
    E3 = models.BooleanField(default=True)
    E4 = models.BooleanField(default=True)
    E5 = models.BooleanField(default=True)
    E6 = models.BooleanField(default=True)
    E7 = models.BooleanField(default=True)
    E8 = models.BooleanField(default=True)
    E9 = models.BooleanField(default=True)
    E10 = models.BooleanField(default=True)
    E11 = models.BooleanField(default=True)
    E12 = models.BooleanField(default=True)
    F1 = models.BooleanField(default=True)
    F2 = models.BooleanField(default=True)
    F3 = models.BooleanField(default=True)
    F4 = models.BooleanField(default=True)
    F5 = models.BooleanField(default=True)
    F6 = models.BooleanField(default=True)
    F7 = models.BooleanField(default=True)
    F8 = models.BooleanField(default=True)
    F9 = models.BooleanField(default=True)
    F10 = models.BooleanField(default=True)
    F11 = models.BooleanField(default=True)
    F12 = models.BooleanField(default=True)
    G1 = models.BooleanField(default=True)
    G2 = models.BooleanField(default=True)
    G3 = models.BooleanField(default=True)
    G4 = models.BooleanField(default=True)
    G5 = models.BooleanField(default=True)
    G6 = models.BooleanField(default=True)
    G7 = models.BooleanField(default=True)
    G8 = models.BooleanField(default=True)
    G9 = models.BooleanField(default=True)
    G10 = models.BooleanField(default=True)
    G11 = models.BooleanField(default=True)
    G12 = models.BooleanField(default=True)
    H1 = models.BooleanField(default=True)
    H2 = models.BooleanField(default=True)
    H3 = models.BooleanField(default=True)
    H4 = models.BooleanField(default=True)
    H5 = models.BooleanField(default=True)
    H6 = models.BooleanField(default=True)
    H7 = models.BooleanField(default=True)
    H8 = models.BooleanField(default=True)
    H9 = models.BooleanField(default=True)
    H10 = models.BooleanField(default=True)
    H11 = models.BooleanField(default=True)
    H12 = models.BooleanField(default=True)
    I1 = models.BooleanField(default=True)
    I2 = models.BooleanField(default=True)
    I3 = models.BooleanField(default=True)
    I4 = models.BooleanField(default=True)
    I5 = models.BooleanField(default=True)
    I6 = models.BooleanField(default=True)
    I7 = models.BooleanField(default=True)
    I8 = models.BooleanField(default=True)
    I9 = models.BooleanField(default=True)
    I10 = models.BooleanField(default=True)
    I11 = models.BooleanField(default=True)
    I12 = models.BooleanField(default=True)
    J1 = models.BooleanField(default=True)
    J2 = models.BooleanField(default=True)
    J3 = models.BooleanField(default=True)
    J4 = models.BooleanField(default=True)
    J5 = models.BooleanField(default=True)
    J6 = models.BooleanField(default=True)
    J7 = models.BooleanField(default=True)
    J8 = models.BooleanField(default=True)
    J9 = models.BooleanField(default=True)
    J10 = models.BooleanField(default=True)
    J11 = models.BooleanField(default=True)
    J12 = models.BooleanField(default=True)
