from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class MatchTypes(models.TextChoices):
    dl_dst = "dl_dst"
    dl_src = "dl_src"
    in_port = "in_port"
    ip_proto = "ip_proto"
    tcp_dst = "tcp_dst"


class ActionTypes(models.TextChoices):
    ALLOW = "allow"
    DENY = "deny"
    REDIRECT = "redirect"
