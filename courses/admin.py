from django.contrib import admin
from .models import Level, Course, Category, Topic, LearningObjective
from lessons.models import StepType, Step, Assignment

class AssignmentInline(admin.StackedInline):
    model = Assignment
    extra = 1

class TopicInline(admin.StackedInline):
    model = Topic
    extra = 1
    exclude = ("teacher",)

class StepInline(admin.StackedInline):
    model = Step
    extra = 1
    exclude = ("teacher",)

class LearningObjectiveInline(admin.TabularInline):
    model = LearningObjective
    extra = 4
    exclude = ("teacher",)

class LearningObjectiveAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
            qs = super(LearningObjectiveAdmin, self).get_queryset(request)
            if request.user.is_superuser:
                return qs
            return qs.filter(teacher=request.user)

    def get_form(self, request, obj=None, **kwargs):
            if request.user.is_superuser:
                self.exclude = ()
            else:
                self.exclude = ('teacher',) 
            return super(LearningObjectiveAdmin, self).get_form(request, obj=None, **kwargs) 

class CourseAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
            qs = super(CourseAdmin, self).get_queryset(request)
            if request.user.is_superuser:
                return qs
            return qs.filter(teacher=request.user)

    def get_form(self, request, obj=None, **kwargs):
            if request.user.is_superuser:
                self.exclude = ()
            else:
                self.exclude = ('teacher',) 
            return super(CourseAdmin, self).get_form(request, obj=None, **kwargs) 

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            instance.teacher = request.user
            instance.save()
        formset.save_m2m()

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            obj.teacher = request.user
        super().save_model(request, obj, form, change)

    inlines = [
        LearningObjectiveInline,
        TopicInline,
    ]


class TopicAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
            qs = super(TopicAdmin, self).get_queryset(request)
            if request.user.is_superuser:
                return qs
            return qs.filter(teacher=request.user)

    def get_form(self, request, obj=None, **kwargs):
            if request.user.is_superuser:
                self.exclude = ()
            else:
                self.exclude = ('teacher',) 
            return super(TopicAdmin, self).get_form(request, obj=None, **kwargs)

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            instance.teacher = request.user
            instance.save()
        formset.save_m2m()
    
    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            obj.teacher = request.user
            super().save_model(request, obj, form, change)
    inlines = [
        StepInline, 
        AssignmentInline,
    ]

class StepAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
            qs = super(StepAdmin, self).get_queryset(request)
            if request.user.is_superuser:
                return qs
            return qs.filter(teacher=request.user)

    def get_form(self, request, obj=None, **kwargs):
            if request.user.is_superuser:
                self.exclude = ()
            else:
                self.exclude = ('teacher',) 
            return super(StepAdmin, self).get_form(request, obj=None, **kwargs) 
    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            obj.teacher = request.user
            super().save_model(request, obj, form, change)

class AssignmentAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
            qs = super(AssignmentAdmin, self).get_queryset(request)
            if request.user.is_superuser:
                return qs
            return qs.filter(teacher=request.user)

    def get_form(self, request, obj=None, **kwargs):
            if request.user.is_superuser:
                self.exclude = ()
            else:
                self.exclude = ('teacher',) 
            return super(AssignmentAdmin, self).get_form(request, obj=None, **kwargs) 
    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            obj.teacher = request.user
            super().save_model(request, obj, form, change)


admin.site.register(Level)
admin.site.register(Category)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(StepType)
admin.site.register(Step, StepAdmin)
admin.site.register(Assignment, AssignmentAdmin)
