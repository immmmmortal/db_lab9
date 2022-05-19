from django.db import models


class Student(models.Model):
    student_pk = models.AutoField(primary_key=True)
    student_group = models.TextField()
    student_full_name = models.TextField()

    def __str__(self):
        return self.student_full_name


class StudentClasses(models.Model):
    student_classes_pk = models.AutoField(primary_key=True)
    student_id = models.ForeignKey('Student', on_delete=models.CASCADE)
    class_id = models.ForeignKey('Classes', on_delete=models.CASCADE)


class Classes(models.Model):
    class_pk = models.AutoField(primary_key=True)
    class_name = models.TextField()
    cathedra = models.TextField()

    def __str__(self):
        return self.class_name


class Teacher(models.Model):
    teacher_pk = models.AutoField(primary_key=True)
    teacher_full_name = models.TextField()

    def __str__(self):
        return self.teacher_full_name


class Workload(models.Model):
    workload_pk = models.AutoField(primary_key=True)
    class_id = models.ForeignKey('Classes', on_delete=models.CASCADE)
    teacher_id = models.ForeignKey('Teacher', on_delete=models.CASCADE)

    def __str__(self):
        return self.teacher_id


class Task(models.Model):
    task_pk = models.AutoField(primary_key=True)
    task_text = models.TextField()
    max_score = models.FloatField()

    def __str__(self):
        return self.task_text


class ClassesTask(models.Model):
    classes_task_pk = models.AutoField(primary_key=True)
    class_id = models.ForeignKey('Classes', on_delete=models.CASCADE)
    task_id = models.ForeignKey('Task', on_delete=models.CASCADE)


class GradedTask(models.Model):
    graded_task_pk = models.AutoField(primary_key=True)
    class_task_id = models.ForeignKey('ClassesTask', on_delete=models.CASCADE)
    student_id = models.ForeignKey('Student', on_delete=models.CASCADE)
    graded_by_teacher_id = models.ForeignKey('Teacher', on_delete=models.CASCADE)
