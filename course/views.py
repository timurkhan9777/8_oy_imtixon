from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User

from .permissions import CustomPermission, TeacherPermission, AdminPermission
from .models import Course, Lesson, LessonVideo, LessonComment, LikeLesson
from .serializers import (CourseSerializer, LessonSerializer, LessonVideoSerializer,
                          EmailSerializer, LessonCommentSerializer, LikeLessonSerializer)

from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class CourseAPIView(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    permission_classes = [AdminPermission]


class LessonAPIView(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']
    permission_classes = [TeacherPermission]


class LessonVideoAPIView(ModelViewSet):
    queryset = LessonVideo.objects.all()
    serializer_class = LessonVideoSerializer
    permission_classes = [TeacherPermission]


class LessonCommentAPIView(ModelViewSet):
    queryset = LessonComment.objects.all()
    serializer_class = LessonCommentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['text']
    permission_classes = [CustomPermission]


class SendtoEmailView(APIView):

    permission_classes = [AdminPermission]

    def post(self, request: Request):

        serializer = EmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        users = User.objects.all()
        users_emails = []

        for user in users:
            users_emails.append(user.email)

        send_mail(
            serializer.validated_data.get("subject"),
            serializer.validated_data.get("message"),
            settings.EMAIL_HOST_USER,
            users_emails,
            fail_silently=False,
        )
        return Response({"message": "success"})


class LikeLessonView(APIView):
    permission_classes = [CustomPermission]

    def get(self, request, pk):
        likes = len(LikeLesson.objects.filter(like_or_dislike=True, lesson_id=pk))
        dislikes = len(LikeLesson.objects.filter(like_or_dislike=False, lesson_id=pk))
        return Response({"likes": likes, "dislikes": dislikes})


class LikeLessonCreateView(APIView):

    permission_classes = [CustomPermission]

    def post(self, request):
        try:
            likes_or_dislikes = LikeLesson.objects.filter(author_id=request.data.get("author"))
            for l_or_d in likes_or_dislikes:
                l_or_d.delete()

        except:
            pass

        serializer = LikeLessonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        like_or_dislike = serializer.save()
        return Response(LikeLessonSerializer(like_or_dislike).data)
