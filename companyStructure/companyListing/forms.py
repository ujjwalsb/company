from django import forms
from .models import CompanyListing, ReviewListing


class CreateCompanyData(forms.ModelForm):

    class Meta:
        model = CompanyListing
        fields = [
            'name',
            'location',
        ]


class CreateReviewData(forms.ModelForm):
    review_date = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = ReviewListing
        fields = [
            'reviewer_name',
            'rating',
            'subject',
            'body',
            'review_date',
        ]
