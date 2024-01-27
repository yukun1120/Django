from django.contrib import admin

from .models import Question

admin.site.register(Question)
# Question オブジェクトがadmin インタフェースを持つ