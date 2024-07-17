from django.contrib import admin
from .models import Course, Lesson, LessonVideo, LessonComment, LikeLesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']
    list_editable = ['name']
    list_display_links = ['pk']


class LessonVideoInline(admin.TabularInline):
    model = LessonVideo
    extra = 0


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['pk', 'course', 'title', 'description', 'created']
    list_editable = ['description']
    list_display_links = ['pk', 'title']

    inlines = [
        LessonVideoInline
    ]


@admin.register(LessonComment)
class LessonCommentAdmin(admin.ModelAdmin):
    list_display = ['pk', 'lesson', 'author', 'text']
    list_editable = ['text']
    list_display_links = ['pk', 'lesson']


@admin.register(LikeLesson)
class LikeLessonAdmin(admin.ModelAdmin):
    list_display = ['pk', 'lesson', 'like_or_dislike', 'author', 'created']
    list_display_links = ['pk', 'lesson']
