from django.db import models
class UserProfile(models.Model):
    name = models.CharField(max_length=100,null=False)
    surname = models.CharField(max_length=100,null=False)
    fathername = models.CharField(max_length=100,null=False)
    address = models.CharField(max_length=100,null=False)
    fincode = models.CharField(max_length=11,null=False)
    register_type=models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=20,null=False)  # Assuming international format
    email = models.EmailField(null=False)
    desc = models.TextField(null=False)
    attachment = models.FileField(upload_to='user_files/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.surname}"
