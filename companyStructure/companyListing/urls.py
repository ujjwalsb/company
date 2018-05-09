from django.conf.urls import url
from companyListing import views

urlpatterns = [
    url(r'^$', views.company_list),
    url(r'^createcompany/$', views.company_create),
    url(r'^review/$', views.review_list),
    url(r'^createreview/$', views.review_create),
]
