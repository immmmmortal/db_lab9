from django.contrib import admin
from tablesUI.models import *


class CustomModelAdmin(admin.ModelAdmin):
    # Subclass for ModelAdmin, automatically display all fields of model in list_display function
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields if field.name != "id"]
        super(CustomModelAdmin, self).__init__(model, admin_site)


class StudentAdmin(CustomModelAdmin):
    pass


admin.site.register(Student, StudentAdmin)


class ClassesAdmin(CustomModelAdmin):
    pass


admin.site.register(Classes, ClassesAdmin)


class TeacherAdmin(CustomModelAdmin):
    pass


admin.site.register(Teacher, TeacherAdmin)


class WorkloadAdmin(CustomModelAdmin):
    pass


admin.site.register(Workload, WorkloadAdmin)


class StudentClassesAdmin(CustomModelAdmin):
    pass


admin.site.register(StudentClasses, StudentClassesAdmin)


class TaskAdmin(CustomModelAdmin):
    pass


admin.site.register(Task, TaskAdmin)


class GradedTaskAdmin(CustomModelAdmin):
    pass


admin.site.register(GradedTask, GradedTaskAdmin)


class ClassesTaskAdmin(CustomModelAdmin):
    pass


admin.site.register(ClassesTask, ClassesTaskAdmin)
