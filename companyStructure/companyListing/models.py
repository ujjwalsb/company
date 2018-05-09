# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class CompanyListing(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    avg_rating = models.PositiveIntegerField(default=0)
    num_review = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class ReviewListing(models.Model):
    reviewer_name = models.CharField(max_length=50)
    rating = models.PositiveIntegerField()
    subject = models.CharField(max_length=100)
    body = models.TextField()
    review_date = models.DateField(auto_now_add=False, auto_now=False)
