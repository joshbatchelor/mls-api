from django.db import models
from mls_api.models.base import BaseModel


class Result(BaseModel):

    DRAW = 'draw'
    WIN = 'win'
    LOSS = 'loss'

    name = models.CharField(max_length=24)
    code = models.SlugField()
    points = models.IntegerField()

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        app_label = 'mls_api'
