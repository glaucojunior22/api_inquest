from rest_framework.routers import DefaultRouter
from . import views


# Change DefaultRouter to remove trailing slash at the end of URL
class OptionalSlashRouter(DefaultRouter):      
    def __init__(self, *args, **kwargs):         
        super(DefaultRouter, self).__init__(*args, **kwargs)         
        self.trailing_slash = '/?'

router = OptionalSlashRouter()

router.register(r'person', views.PersonViewSet)
router.register(r'enterprise', views.EnterpriseViewSet)
router.register(r'possession', views.PossessionViewSet)

api_urlpatterns = router.urls
