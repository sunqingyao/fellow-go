from django.conf.urls import url

from . import views

app_name = 'pickup'

urlpatterns = [
    url(r'^$',
        views.OrderFilterView.as_view(),
        name='order-list'),
    url(r'^detail/(?P<pk>[0-9])/$',
        views.OrderFilterView.as_view(),
        name='order-detail')
]