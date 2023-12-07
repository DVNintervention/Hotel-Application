# tenantspecific/models.py
from django.db import models

class Guest(models.Model):
    name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)
    email_address = models.EmailField()

    def __str__(self):
        return self.name

class Reservation(models.Model):
    guest = models.ForeignKey('Guest', on_delete=models.CASCADE)
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()
    room_number = models.CharField(max_length=10)

    def __str__(self):
        return "%s reservation from %s to %s" % (self.guest.name, self.check_in_date, self.check_out_date)


class RoomServiceOrder(models.Model):
    reservation = models.ForeignKey('Reservation', on_delete=models.CASCADE)
    service_details = models.TextField()
    request_time = models.DateTimeField()
    delivery_time = models.DateTimeField(blank=True, null=True)
    charge = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return "Order #{} - {}".format(self.id, self.service_details)



class Payment(models.Model):
    reservation = models.ForeignKey('Reservation', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_date = models.DateTimeField()
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return "Payment {} for Reservation {}".format(self.id, self.reservation.id)



class CleaningCrew(models.Model):
    name = models.CharField(max_length=255)
    shift_start = models.TimeField()
    shift_end = models.TimeField()
    assigned_rooms = models.TextField()  # Consider using a more structured approach, like a ManyToManyField relationship for scalability and data integrity.

    def __str__(self):
        return self.name

class Administrator(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    email_address = models.EmailField()

    def __str__(self):
        return "{} - {}".format(self.role, self.name)


