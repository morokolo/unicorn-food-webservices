from django.conf.urls import url

from menu import views

urlpatterns = [
    url(r'restaurant/(?P<restaurant>[0-9]+)/items$', views.MenuItemsByRestaurantId.as_view(), name='menu_items'),

    # url(r'^(?P<pk>[0-9]+)/matters/$', views.project_matters, name='project_matters'),
    # url(r'^detail/(?P<pk>[0-9]+)/$', views.ProjectDetail.as_view(), name='project_detail'),
    # url(r'^change-status/(?P<pk>[0-9]+)/$', views.project_change_status, name='project_change_status'),
    # url(r'^(?P<pk>[0-9]+)/edit(?:/(?P<future_revision_id>[0-9]+))?/$', views.edit_project, name='edit_project'),
    # url(r'^add/$', views.project_create_details, name='add_project'),
    # url(r'^(?P<pk>[0-9]+)/deliverables/$', views.project_create_deliverables, name='deliverables'),
    # url(r'^(?P<pk>[0-9]+)/matters/export/$', views.export_matters, name='export_matters'),
    # url(r'^(?P<pk>[0-9]+)/entities/$', views.project_link_entities, name='entities'),
    # url(r'^(?P<pk>[0-9]+)/entities/add/$', views.add_entities, name='add_entities'),
    # url(r'^(?P<pk>[0-9]+)/entities/edit/$', views.edit_entities, name='edit_entities'),
    # url(r'^(?P<pk>[0-9]+)/products/$', views.project_link_products, name='products'),
    # url(r'^(?P<pk>[0-9]+)/products/add/$', views.add_products, name='add_products'),
    # url(r'^(?P<pk>[0-9]+)/revision/(?P<project_revision_id>[0-9]+)/products/edit/$', views.edit_products,
    #     name='edit_products'),
    # url(r'^(?P<pk>[0-9]+)/trace-pack/$', views.create_trace_pack, name='trace_pack'),
    # url(r'^(?P<pk>[0-9]+)/trace-pack/edit/$', views.edit_trace_pack, name='edit_trace_pack'),
    # url(r'^', views.ProjectList.as_view(), name='project_dashboard'),
]
