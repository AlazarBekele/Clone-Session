from django.db import models

# Create your models here.

class JobDepartement (models.Model):

  name = models.CharField(max_length=50)
  description = models.TextField()

  def __str__(self) -> str:
    return self.name
  

class Apply(models.Model):

  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=30)
  dob = models.DateField(auto_now_add=False, auto_now=False)
  detail_about = models.TextField()
  job_departement = models.ForeignKey(JobDepartement,on_delete=models.SET_NULL, null=True)


  def __str__(self) -> str:
    return self.first_name + self.last_name