from django.conf.urls import patterns, url
from classifier import views

urlpatterns = patterns('classifier.views',
    #classifiers
    url(r'^classifier/$', views.ClsList.as_view()),
    url(r'^classifier/(?P<cls_id>[0-9]+)$', views.ClsDetail.as_view()),
    url(r'^classifier/(?P<cls_id>[0-9]+)/train_vector/$', views.VectorList.as_view()),
)