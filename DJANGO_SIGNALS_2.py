##This is an example code snippet.
##Here we need to threading module to display the thread used in the caller and signal_handler
##So if we execute we can see both my_signal_handler and create_user uses same thread.So answer is yes.
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Signal handler
@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal handler running in thread: {threading.current_thread().name}")

# Some function that saves a user, which triggers the signal
def create_user():
    print(f"Function running in thread: {threading.current_thread().name}")
    user = User.objects.create(username="testuser")
    user.save()

# Call the function
if __name__ == "__main__":
    create_user()

##Output will be like:-
#Function running in thread: MainThread
#Signal handler running in thread: MainThread

