from django.db import models
from django import forms
from hashlib import md5


class Mapper(models.Model):
    "A class to map IP and names"
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100, unique=True)
    poweron = models.BooleanField(default=False)
    ip = models.GenericIPAddressField(default='0.0.0.0')
    password = models.CharField(max_length=100, null=True)
    pass_hash = models.CharField(max_length=100, default='None')

    stamp = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.password is not None:
            passwd = self.password
            self.password = None
            bts = passwd.encode('utf-8')
            this_hash = md5(bts).hexdigest()
            self.pass_hash = this_hash
        super(Mapper, self).save(*args, **kwargs)

    def checkpwd(self, passwd):
        "Check if the passwd is correct"
        assert isinstance(passwd, str)
        bts = passwd.encode('utf-8')
        this_hash = md5(bts).hexdigest()
        return this_hash == self.pass_hash

    def setpwd(self, passwd):
        "Set password"
        assert isinstance(passwd, str)
        bts = passwd.encode('utf-8')
        this_hash = md5(bts).hexdigest()
        self.pass_hash = this_hash
        self.save()

    def setip(self, ip, passwd):
        if self.checkpwd(passwd):
            self.ip = ip
            self.save()


class MapperForm(forms.ModelForm):
    class Meta:
        model = Mapper
        fields = ['name', 'password']
