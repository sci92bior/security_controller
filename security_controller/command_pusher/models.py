from datetime import datetime

from django.db import models

from security_controller.common.models import TimestampedModel



class Switch(TimestampedModel):
    manufacturer = models.CharField(max_length=50)
    hardware = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50)
    connected = models.BooleanField(default=False)
    dpid = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.dpid + " " + self.manufacturer + " " + self.hardware + " " + self.serial_number

    class Meta:
        verbose_name = "Switch"
        verbose_name_plural = "Switches"



class Match(models.Model):
    dl_dst = models.CharField(max_length=17, null=True, blank=True)  # Adjust max length based on MAC address format
    dl_src = models.CharField(max_length=17, null=True, blank=True)  # Adjust max length based on MAC address format
    in_port = models.IntegerField(null=True, blank=True)
    ip_proto = models.IntegerField(null=True, blank=True)
    tcp_dst = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Match for dl_dst={self.dl_dst}, dl_src={self.dl_src}, in_port={self.in_port}"


class Action(models.Model):
    type = models.CharField(max_length=20)
    port = models.CharField(max_length=20)# Adjust max length as needed

    def __str__(self):
        return self.type + ":" + str(self.port)


class FlowEntry(models.Model):
    switch = models.ForeignKey(Switch, on_delete=models.PROTECT)  # Create a one-to-many relationship with the Switch model
    actions = models.ManyToManyField(Action,null=True, blank=True)  # Create a many-to-many relationship with the Action model
    idle_timeout = models.IntegerField(null=True, blank=True)
    cookie = models.IntegerField(null=True, blank=True)
    packet_count = models.IntegerField(null=True, blank=True)
    hard_timeout = models.IntegerField(null=True, blank=True)
    byte_count = models.IntegerField(null=True, blank=True)
    duration_sec = models.IntegerField(null=True, blank=True)
    duration_nsec = models.IntegerField(null=True, blank=True)
    priority = models.IntegerField(null=True, blank=True)
    length = models.IntegerField(null=True, blank=True)
    flags = models.IntegerField(null=True, blank=True)
    table_id = models.IntegerField(null=True, blank=True)
    match = models.OneToOneField(Match, on_delete=models.CASCADE, null=True, blank=True, related_name='flowentry')  # Create a one-to-one relationship with the Match model

    def __str__(self):
        return self.switch.dpid
