from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ValidationError
from phonenumber_field.modelfields import PhoneNumberField

## make_password is used to hash password before storing in database, check_password may be used to verify password entered to match hashed password.

class User(models.Model):
    Identification_ID=models.AutoField(primary_key=True)        ## Identification number for each user
    name=models.CharField(max_length=80,null=False)             
    email=models.EmailField(null=True,blank=True)
    password=models.CharField(max_length=128,null=False)        ##  Password hashed using make_password for security
    number=PhoneNumberField(null=False,unique=False)            ## PhoneNumberField used for input for telephone number
    personal_number=PhoneNumberField(null=True,unique=False,blank=True)
    registered_user=models.BooleanField(default=True)
    spam=models.BooleanField(default=False)

    HARDCODED_NAME = "Nabeel"       ## one user is alloted a particular phone number which cannot be taken by another user
    HARDCODED_NUMBER = "+911234567890"

    def save(self, *args, **kwargs):
        ## Hash the password before saving
        self.password = make_password(self.password)

        ## Validate phone number and name constraints
        if self.number == self.HARDCODED_NUMBER and self.name != self.HARDCODED_NAME:
            raise ValidationError(f"The number {self.HARDCODED_NUMBER} can only be assigned to {self.HARDCODED_NAME}.")

        if self.name == self.HARDCODED_NAME and self.number != self.HARDCODED_NUMBER:
            raise ValidationError(f"The name {self.HARDCODED_NAME} must be associated with the number {self.HARDCODED_NUMBER}.")

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name