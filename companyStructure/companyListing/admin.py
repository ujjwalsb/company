# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import CompanyListing, ReviewListing


class CompanyModelAdmin(admin.ModelAdmin):
    list_display = ["name", "location"]
    list_filter = ["location"]

    class Meta:
        model = CompanyListing


admin.site.register(CompanyListing, CompanyModelAdmin)


class ReviewModelAdmin(admin.ModelAdmin):
    list_display = ["reviewer_name", "rating", "review_date"]
    list_filter = ["rating", "review_date"]

    class Meta:
        model = ReviewListing


admin.site.register(ReviewListing, ReviewModelAdmin)
