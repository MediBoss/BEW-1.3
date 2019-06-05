from django.db import models

# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def set_price(self):
        
        if self.size == 'small':
            self.price = 10.30

        elif self.size == 'medium':
            self.price = 15.30

        elif self.size == 'large':
            self.prize = 20.30

        return self.price


class Toping(models.Model):
    name = models.CharField(max_length=20)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)


