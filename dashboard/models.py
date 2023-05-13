import uuid
from django.db import models

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Task(models.Model):
    STATUS_OPTIONS = (
        ('concluido', 'Concluído'),
        ('pendente', 'Pendente'),
        ('adiado', 'Adiado'),
        ('em_andamento', 'Em andamento')
    )
    
    CATEGORY_OPTIONS = (
        ('urgente', 'Urgente'),
        ('importante', 'Importante'),
        ('precisa_ser_feito', 'Precisa ser feito')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=125)
    description = models.CharField(max_length=400)
    create_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=25, choices=CATEGORY_OPTIONS, default='importante')
    status = models.CharField(max_length=25, choices=STATUS_OPTIONS, default='pendente')
    
    def __str__(self):
        return self.title
