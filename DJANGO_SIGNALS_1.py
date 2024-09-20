##This is an example code snippet.
import time
from django.dispatch import Signal, receiver


# Defining a custom signal in signals.py file
my_signal = Signal()

# Signal handler
@receiver(my_signal)
def my_signal_handler(sender, **kwargs):
    print("Signal handler started.")
    time.sleep(5)  # Simulating a long-running process
    print("Signal handler completed.")

# Then will create a view 
from django.http import HttpResponse
from .signals import my_signal

def trigger_signal(request):
    print("Before sending signal.")
    # Sending the signal
    my_signal.send(sender=None)
    print("After sending signal.")
    return HttpResponse("Signal triggered")

##Here if we run the code we can see that by default, Django signals are executed synchronously. This means the signal handler runs in the same thread and process as the function that sends the signal. The sender waits for the signal handlers to complete before proceeding.

##Here if we trigger signal while signal is send first signal_handler will executed completely then the whole process will be completed.

##Here the result will be like :- Before sending signal.
#Signal handler started.
# 5 seconds delay here...
#Signal handler completed.
#After sending signal.
