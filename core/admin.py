from django.contrib import admin

# Register your models here.
from .models import Answer
from .models import Category
from .models import Question
from .models import Quiz
from .models import QuizResponse

# register the models
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Quiz)
admin.site.register(QuizResponse)
admin.site.register(Category)
