from django.db import models
from django.conf import settings

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

    title = models.CharField(max_length=30, verbose_name='titre_du_projet')
    description = models.TextField(max_length=2048, verbose_name='description_du_projet')
    type = models.CharField(max_length=30, choices=TYPE_CHOICES, verbose_name='Type_de_projet')
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE, related_name='auteur_projet')

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
    project = models.ForeignKey(Projects,
                              on_delete=models.CASCADE, 
                              related_name='projet')
    created_time = models.DateTimeField(auto_now_add=True, null=True)
    description = models.TextField(max_length=2048, 
                                   verbose_name='description_du_probleme')
    status = models.CharField(max_length=30, 
                              choices=TYPE_CHOICES_STATUS, 
                              verbose_name='priorite')
    priority = models.CharField(max_length=30, 
                                choices=TYPE_CHOICES_PRIORITY, 
                                verbose_name='priorite')
    balise = models.CharField(max_length=30, 
                              choices=TYPE_CHOICES_BALISE, 
                              verbose_name='balise')
    assignee_user =  models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        primary_key=True,
        related_name="utilisateur_affecté")
    
class Comments(models.Model):
    description = models.TextField(max_length=2048, verbose_name='description_du_commentaire')
    issue = models.ForeignKey(Issues, 
                                on_delete=models.CASCADE, 
                                related_name='projet')
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE, 
                              related_name='auteur_comment') 