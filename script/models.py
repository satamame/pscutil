import uuid
from django.db import models

class Script(models.Model):
    '''Keeps script data during page transition
    '''
    token = models.UUIDField(
        'token', primary_key=True, default=uuid.uuid4, editable=False)
    create_dt = models.DateTimeField('created', auto_now_add=True)
    modify_dt = models.DateTimeField('modified', auto_now=True)
    plain_text = models.TextField('plain_text', blank=False)
    line_types = models.TextField('line_types', blank=True)
    formatted = models.TextField('formatted', blank=True)
    FORMAT_CHOICES = (
        (1, 'Fountain JA'),
    )
    format = models.IntegerField('format', default=1, choices=FORMAT_CHOICES)
