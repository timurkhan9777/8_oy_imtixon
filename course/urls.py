from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from .views import (CourseAPIView, LessonAPIView, LessonVideoAPIView, SendtoEmailView,
                    LessonCommentAPIView, LikeLessonView, LikeLessonCreateView)
from rest_framework import routers

router = routers.DefaultRouter()
router.register("course", CourseAPIView)
router.register("lesson", LessonAPIView)
router.register("lesson-video", LessonVideoAPIView)
router.register("comment", LessonCommentAPIView)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/email/', SendtoEmailView.as_view()),

    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/accounts/', include('rest_registration.api.urls')),
    path('api/v1/lesson/<int:pk>/like/', LikeLessonView.as_view()),
    path('api/v1/lesson/like/create/', LikeLessonCreateView.as_view()),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]