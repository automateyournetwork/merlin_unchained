from django.contrib import admin

from . import models

admin.site.register(models.Devices)
admin.site.register(models.DynamicJobInput)
admin.site.register(models.LearnACL)
admin.site.register(models.LearnARP)
admin.site.register(models.LearnARPStatistics)
admin.site.register(models.LearnBGPInstances)
admin.site.register(models.LearnBGPRoutesPerPeer)
admin.site.register(models.LearnBGPTables)
admin.site.register(models.LearnInterface)
admin.site.register(models.LearnVLAN)
admin.site.register(models.LearnVRF)
admin.site.register(models.ShowInventory)
admin.site.register(models.ShowIPIntBrief)
admin.site.register(models.ShowVersion)