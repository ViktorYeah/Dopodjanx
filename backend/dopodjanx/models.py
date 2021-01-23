from django.db import models

class CompanyInfo(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200)
    DateTime = models.DateField()
    Employees = models.IntegerField()
    Assets = models.IntegerField()
    Link = models.CharField(max_length=500)

    def __str__(self):
        return self.Name
    