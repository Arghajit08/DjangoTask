##This is an example code snippet.
# models.py
#There are 4 types of django signals :- pre_save,post_save,pre_delete_post_delete
#Yes, Django signals (like post_save or pre_save) run in the same database transaction as the caller by default. If an exception occurs during a signal handler, it can roll back the entire transaction initiated by the calling code.
from django.db import models
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyModel(models.Model):
    name = models.CharField(max_length=100)

# Signal that throws an exception to test transaction rollback
@receiver(post_save, sender=MyModel)
def my_model_post_save(sender, instance, **kwargs):
    print(f"Signal triggered for {instance.name}")
    raise Exception("Error in signal handler")

# views.py
from django.http import JsonResponse
from django.shortcuts import render
from .models import MyModel

def test_signal_transaction(request):
    try:
        with transaction.atomic():
            obj = MyModel.objects.create(name="Test Name")
            print("Model saved successfully")
    except Exception as e:
        print(f"Exception caught: {e}")

    # Check if the object was saved in the database
    exists = MyModel.objects.filter(name="Test Name").exists()
    return JsonResponse({"exists": exists})

