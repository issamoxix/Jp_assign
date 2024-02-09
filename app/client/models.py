from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

class LegalRequest(models.Model):
    STATUS_CHOICES = (
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('rejected', 'Rejected'),
    )

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    case_description = models.TextField()
    case_type = models.CharField(max_length=100)
    submission_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

class DocumentAttachment(models.Model):
    legal_request = models.ForeignKey(LegalRequest, on_delete=models.CASCADE)
    document = models.FileField(upload_to='documents/')
