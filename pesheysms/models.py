from django.db import models

class Users(models.Model):
    firstname = models.CharField(max_length=30, blank=False, null=False)
    lastname = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField()
    password = models.CharField(max_length=100, blank=False, null=False)
    # Password field is inherited from AbstractUser

    # Add any additional fields or methods as needed
    class Meta:
        app_label = 'pesheysms'

class UploadedCSV(models.Model):
    useremail = models.EmailField()
    filename = models.CharField(max_length=255)
    customfilename = models.CharField(max_length=255)
    createdat = models.DateTimeField(auto_now_add=True)
    mobilecount = models.PositiveIntegerField()

    def __str__(self):
        return self.customfilename


class getsenderid(models.Model):
    useremail = models.EmailField()
    senderid = models.CharField(max_length=255)
    smstype = models.CharField(max_length=255)
    serviceprovider = models.CharField(max_length=255, default="safaricom")
    applicationletter = models.CharField(max_length=255)
    cr12 = models.CharField(max_length=255)
    cr13 = models.CharField(max_length=255)
    certincorp = models.CharField(max_length=255)
    bussinesscert = models.CharField(max_length=255)
    requestedon = models.CharField(max_length=255)
    approvedon = models.CharField(max_length=255)
    status = models.CharField(max_length=50, default="Pending")  

    def __str__(self):
        return self.customfilename
