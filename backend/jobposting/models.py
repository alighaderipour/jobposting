from django.db import models

# Create your models here.
class JobPosting(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100)
    salary = models.IntegerField()
    is_active = models.BooleanField(default=False)

    class Meta:
        db_table = 'jobposting'  # 👈 This tells Django to use your existing table

    def __str__(self):
        return f"{self.title} | {self.company} | {'Active' if self.is_active else 'Not Active'}"