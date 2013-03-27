from django.db import models

class MessageData(models.Model):
    msg_id = models.CharField(primary_key=True, max_length=100)
    sender = models.CharField(max_length=100)
    sent_on = models.DateTimeField(auto_now=False, auto_now_add=False)
    subject = models.CharField(max_length=1000)
    text = models.TextField()
    ordinal = models.SmallIntegerField()

