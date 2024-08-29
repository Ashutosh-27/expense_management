from django.db import models

# Create your models here.
class TblUsers(models.Model):
    u_id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    u_email = models.EmailField(unique=True, max_length=255)  # Email field with unique constraint
    u_password = models.CharField(max_length=255)  # Password field
    created_at = models.DateTimeField(auto_now_add=True)  # DateTime field with auto-insert current time

    def __str__(self):
        return self.u_email