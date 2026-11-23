from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from .models import Order,Dish


@receiver(post_save,sender=Order)
@receiver(post_delete,sender=Order)
def update_order_count(sender,instance,**kwargs):
    count = Order.objects.filter(dish_id=instance.dish_id).count()
    Dish.objects.filter(id=instance.dish_id).update(orders_count=count)