from django.conf.urls import url, include
from .views import all_products, view_necklaces, view_pendants, view_earrings, view_bracelets, view_rings, view_sets 

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^$', view_necklaces, name='necklaces'),
    url(r'^$', view_necklaces, name='pendants'),
    url(r'^$', view_necklaces, name='earrings'),
    url(r'^$', view_necklaces, name='bracelets'),
    url(r'^$', view_necklaces, name='rings'),
    url(r'^$', view_necklaces, name='sets'),
]