#  post means after
from django.db.models.signals import post_save, post_delete
#  to receive these signals
from django.dispatch import receiver

from .models import OrderLineItem


#  decorater ensures that we are receiving post saves
#  signals from the OrderLineItem model
@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem create/update
    """
    #  instance order refers to the order this
    #  specific line item is related to
    instance.order.update_total()


#  decorater ensures that we are receiving post deletes
#  signals from the OrderLineItem model
@receiver(post_delete, sender=OrderLineItem)
def delete_on_save(sender, instance, **kwargs):
    #  created by param removed as it isn't
    #  sent by this signal
    """
    Update order total on lineitem create/update
    """
    #  instance order refers to the order this
    #  specific line item is related to
    instance.order.update_total()
