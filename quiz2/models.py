from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import User

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=255, default='Name')
    description = models.TextField(max_length=255, default='Description')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['-id']

    def __str__(self):
        return self.name

    
class Updated(models.Model):
    date_updated = models.DateTimeField(verbose_name='Last updated', auto_now=True)

    class Meta:
        abstract = True


class Quiz(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, default='')
    title = models.ForeignKey(Category, default=1, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255, default='', verbose_name= 'Quiz Name')
    description = models.TextField(default='Description of the Quiz')

    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizzes'
        ordering = ['-id']
    
    def __str__(self):
        return self.author

class Question(Updated):
    topic = models.CharField(max_length=255, default='Topic of Quiz')

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        ordering = ['-id']


    LEVEL = [
        (1, 'Beginner'),
        (2, 'Intermediate'),
        (3, 'Advanced'),
        (4, 'Expert'),
        (5, 'Master'),
    ]

    TYPE = (
        (0, 'Multiple Choice'),
    )

    quiz = models.ForeignKey(Quiz, related_name = 'question', on_delete=models.DO_NOTHING)
    technique = models.IntegerField(choices=TYPE, default=0, verbose_name= 'Type of Question')
    title = models.CharField(max_length=255, verbose_name = 'Questions')
    difficulty = models.CharField(choices=LEVEL, default=0, verbose_name = 'Difficulty', max_length=255)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name= 'Date Created')
    is_active = models.BooleanField(default=False, verbose_name = 'Active Status')
    
    def __str__(self):
        return self.topic


class Answer(Updated):

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
        ordering = ['-id']

    question = models.ForeignKey(Question, related_name= 'answers', on_delete=models.DO_NOTHING, null=True)
    answer_text = models.CharField(max_length=255, default='', verbose_name= 'Answer Text')
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text

