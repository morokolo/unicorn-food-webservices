from __future__ import unicode_literals


class OrderItem(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    description = models.CharField(max_length=200, blank=False, null=False)
    restaurant = models.ForeignKey(Restaurant)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.title

class Order(models.Model):