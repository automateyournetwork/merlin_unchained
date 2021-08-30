from django.db import models

class ShowVersion(models.Model):
    bootflash = models.TextField()
    chassis = models.TextField()
    cpu = models.TextField()
    device_name = models.TextField()
    memory = models.TextField()
    model = models.TextField()
    processor_board_id = models.TextField()
    rp = models.TextField()
    slots = models.TextField()
    days = models.TextField()
    hours = models.TextField()
    minutes = models.TextField()
    seconds = models.TextField()
    name = models.TextField()
    os = models.TextField()
    reason = models.TextField()
    system_compile_time = models.TextField()
    system_image_file = models.TextField()
    system_version = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        template = '{0.bootflash} {0.chassis} {0.cpu} {0.device_name} {0.memory} {0.model} {0.processor_board_id} {0.rp} {0.slots} {0.days} {0.hours} {0.minutes} {0.seconds} {0.name} {0.os} {0.reason} {0.system_compile_time} {0.system_image_file} {0.system_version} {0.timestamp}'
        return template.format(self)