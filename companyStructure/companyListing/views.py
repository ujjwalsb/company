# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import CompanyListing, ReviewListing
from .forms import CreateCompanyData, CreateReviewData
from django.http import HttpResponseRedirect
from .filters import LocationFilter


def company_create(request):
    companydata = CreateCompanyData(request.POST or None)
    if companydata.is_valid():
        instance = companydata.save(commit=False)
        instance.save()
        return HttpResponseRedirect('/')
    context = {
        "title": "Create Company Data",
        "form": companydata,
    }
    return render(request, 'company_create.html', context)


def company_list(request):
    queryset = CompanyListing.objects.all()
    location_filter = LocationFilter(request.GET, queryset)
    review = ReviewListing.objects.count()
    context = {
        "title": "Company List",
        "data_values": queryset,
        "filter": location_filter,
        "review": review,
    }
    return render(request, 'company_list.html', context)


def review_create(request):
    reviewdata = CreateReviewData(request.POST or None)
    if reviewdata.is_valid():
        instance = reviewdata.save(commit=False)
        instance.save()
        return HttpResponseRedirect('/review/')
    context = {
        "title": "Create Review",
        "form": reviewdata,
    }
    return render(request, 'review_create.html', context)


def review_list(request):
    queryset = ReviewListing.objects.all()
    qs_company = CompanyListing.objects.all()
    context = {
        "title": "Review List",
        "data_values": queryset,
        "company_values": qs_company,
    }
    return render(request, 'review_list.html', context)
