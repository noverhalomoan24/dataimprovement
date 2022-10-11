from django.db import models

# Create your models here.


class CardFeeling(models.Model):
    feeling = models.CharField(max_length=255)
    describe = models.CharField(max_length=2500)
    tglupdate = models.DateTimeField(auto_now=True)



class quotesFelling(models.Model):
    hastegquotes = models.CharField(max_length=1000)
    quotesdesc = models.CharField(max_length=1000)
    quoteupdate = models.DateTimeField(auto_now=True)

class temp_json(models.Model):
    name_file = models.CharField(max_length=200)
    the_json = models.JSONField()
    def __str__(self):
        return self.name_file

# class analisis_json(models.Model):
#     name_file_an = models.CharField(max_length=200)
#     the_json_an = models.JSONField()
#
#     def __str__(self):
#         return self.name_file_an


class SaleryOfData(models.Model):
    def number():
        no = SaleryOfData.objects.count()
        if no == None:
            return 1
        else:
            return no + 1

    id_salery = models.IntegerField(unique=True,default=number)
    Experience = models.DecimalField(max_digits=10, decimal_places=3)
    Salery = models.DecimalField(max_digits=10, decimal_places=3)


