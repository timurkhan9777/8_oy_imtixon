from rest_framework import serializers
from .models import Course, Lesson, LessonVideo, LessonComment, LikeLesson


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name']


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'course', 'title', 'description', 'created']


class LessonVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonVideo
        fields = ['id', 'lesson', 'video', 'created']


class LessonCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonComment
        fields = ['id', 'lesson', 'author', 'text']


class EmailSerializer(serializers.Serializer):
    subject = serializers.CharField(max_length=255)
    message = serializers.CharField()


class LikeLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeLesson
        fields = '__all__'


