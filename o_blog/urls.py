from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from o_blog import settings
from graphene_django.views import GraphQLView
from django.conf import settings
from blog.schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^graphql', GraphQLView.as_view(graphiql=settings.DEBUG, schema=schema)),
    path('', include('blog.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns