import imp
from django.contrib import admin

from rclone_api import models


admin.site.register(models.UserProfile)