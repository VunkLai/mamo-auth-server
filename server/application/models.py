from __future__ import annotations

import os
from hashlib import sha1, sha256

from django.db import models
from django.utils import timezone


def encrypt_module(name: str) -> tuple[str, str]:
    salt = os.urandom(64)
    now = timezone.localtime().timestamp()
    salted_name = f"{salt}{name}{now}".encode("utf-8")
    return (sha1(salted_name).hexdigest(), sha256(salted_name).hexdigest())


class ApplicationManager(models.Manager):
    def register(self, name: str, redirect_urls: str) -> Application:
        client_id, client_secret = encrypt_module(name)
        print(
            "id", client_id, "secret", client_secret, "name", name, "r", redirect_urls
        )
        obj = self.model(
            name=name,
            redirect_urls=redirect_urls,
            client_id=client_id,
            client_secret=client_secret,
        )
        obj.save()
        return obj


class Application(models.Model):
    name = models.CharField(max_length=119, db_index=True)
    redirect_urls = models.TextField()
    client_id = models.CharField(max_length=40, unique=True)
    client_secret = models.CharField(max_length=64)

    objects = ApplicationManager()

    def refresh(self) -> None:
        _, client_secret = encrypt_module(self.name)
        self.client_secret = client_secret
        self.save()
