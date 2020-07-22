from django.db import models




class equipments(models.Model):
    equipment_name = models.CharField(max_length=15)
    model_number = models.IntegerField()
    equipment_type = models.CharField(max_length=20)
    #station_name = models.ForeignKey(station,on_delete=models.CASCADE)
    station_name = models.CharField(max_length=20)
    #Qr_code = models.ForeignKey(qr_image, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural="QRCODEDATA"
    def __str__(self):
        return f'{self.equipment_name}'

class qr_image(models.Model):
    #eq = equipments()
    #equipment =models.ForeignKey(eq.equipment_name,on_delete=models.CASCADE)
    Qr_code = models.ImageField(upload_to='media')



