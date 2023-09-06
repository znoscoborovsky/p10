from django.db import models
from django.conf import settings
import uuid

class Projects(models.Model):
    BACK_END = "BACK_END"
    FRONT_END = "FRONT_END"
    IOS = "IOS"
    ANDROID = "ANDROID"

    TYPE_CHOICES = (
        (BACK_END , "BACK_END"),
        (FRONT_END , "FRONT_END"),
        (IOS , "IOS"),
        (ANDROID , "ANDROID"),
    )
    created_time = models.DateTimeField(auto_now_add=True, null=True)
    title = models.CharField(max_length=100, verbose_name='titre du projet')
    description = models.TextField(max_length=2048, verbose_name='description du projet')
    type = models.CharField(max_length=30, choices=TYPE_CHOICES, verbose_name='Type de projet')
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE, related_name='author_projet')

    def __str__(self):
        return self.title
    
class Issues(models.Model):
    BUG = "BUG"
    TASK = "TASK"
    FEATURE = "FEATURE"

    TYPE_CHOICES_BALISE = (
        (BUG , "BUG"),
        (TASK , "TASK"),
        (FEATURE , "FEATURE"),
    )

    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"

    TYPE_CHOICES_PRIORITY = (
        (LOW , "LOW"),
        (MEDIUM , "MEDIUM"),
        (HIGH , "HIGH"),
    )

    TO_DO = "TO_DO"
    IN_PROGRESS = "IN_PROGRESS"
    FINISHED = "FINISHED"

    TYPE_CHOICES_STATUS = (
        (TO_DO , "TO_DO"),
        (IN_PROGRESS , "IN_PROGRESS"),
        (FINISHED , "FINISHED"),
    )
    
    created_time = models.DateTimeField(auto_now_add=True, null=True)
    title = models.CharField(max_length=100, verbose_name='titre de la tache')
    project = models.ForeignKey(Projects,
                              on_delete=models.CASCADE, 
                              related_name='project')
    description = models.TextField(max_length=2048, 
                                   verbose_name='description du probleme')
    status = models.CharField(max_length=30, 
                              choices=TYPE_CHOICES_STATUS, 
                              verbose_name='statut')
    priority = models.CharField(max_length=30, 
                                choices=TYPE_CHOICES_PRIORITY, 
                                verbose_name='priorite')
    balise = models.CharField(max_length=30, 
                              choices=TYPE_CHOICES_BALISE, 
                              verbose_name='balise')
    assignee_user =  models.ForeignKey(
                                    settings.AUTH_USER_MODEL, 
                                    on_delete=models.CASCADE,
                                    related_name="assigne")
    
class Comments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, verbose_name='titre du commentaire')    
    created_time = models.DateTimeField(auto_now_add=True, null=True)
    description = models.TextField(max_length=2048, verbose_name='description du commentaire')
    issue = models.ForeignKey(Issues, 
                                on_delete=models.CASCADE, 
                                related_name='comment')
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE, 
                              related_name='auteur_comment') 