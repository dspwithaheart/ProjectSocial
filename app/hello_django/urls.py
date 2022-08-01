from django.contrib import admin

from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static

from upload.views import image_upload, MyTokenObtainPairView
from upload.models import Entry, IdToken

from django.conf.urls import url

from rest_framework import permissions
from rest_framework import routers, serializers, viewsets
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework_simplejwt import views as jwt_views
from rest_framework.permissions import IsAuthenticated

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
    # permission_classes = [IsAuthenticated]
)



# Serializers define the API representation.
class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = '__all__'

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdToken
        fields = '__all__'
        
# ViewSets define the view behavior.
class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    filterset_fields = '__all__'

class TokenViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = IdToken.objects.all()
    serializer_class = TokenSerializer
    filterset_fields = '__all__'



# Definition of REST endpoints
router = routers.DefaultRouter()
router.register(r'entry', EntryViewSet)
# router.register(r'token', TokenViewSet)


urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("upload/", image_upload, name="upload"),
    path("admin/", admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # JWT URLs...
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/customtoken/', MyTokenObtainPairView.as_view(), name='token_refresh'),
]


if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
