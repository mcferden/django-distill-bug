from django.contrib import admin
from django_distill.renderer import render_to_dir  # this import breaks Django's URL resolution

from web.models import Test


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    pass
