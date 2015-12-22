# -*- coding: utf-8 -*-
from datetime import datetime
from django.contrib.auth.models import User
from django.db import models


class Transaction(models.Model):
    title = models.CharField("Title", max_length=255, blank=False)
    creditor = models.ForeignKey(User, verbose_name="Creditor", related_name="Creditor")
    debitors = models.ManyToManyField(User, verbose_name="Debitors", related_name="Debitors")
    amount = models.FloatField("Amount", blank=False)
    created = models.DateTimeField('Created', default=datetime.now)
