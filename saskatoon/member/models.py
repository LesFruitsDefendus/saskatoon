# coding: utf-8

from django.db import models
from django.template.defaultfilters import register
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import RegexValidator

from harvest.models import RequestForParticipation


class AuthUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(username=username, email=self.normalize_email(email),
                          )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(username=username, email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

@python_2_unicode_compatible
class AuthUser(AbstractBaseUser, PermissionsMixin):

    person = models.OneToOneField('Person', null=True)

    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', message='Only alphanumeric characters are allowed.')

    # Redefine the basic fields that would normally be defined in User
    email = models.EmailField(verbose_name='email address', unique=True, max_length=255)

    # Our own fields
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True, null=False)
    is_staff = models.BooleanField(default=False, null=False)

    objects = AuthUserManager()
    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        try:
            return u"%s" % (self.person)
        except:
       	    return self.email


@python_2_unicode_compatible
class Actor(models.Model):
    actor_id = models.AutoField(
        primary_key=True
    )

    class Meta:
        verbose_name = _("actor")
        verbose_name_plural = _("actors")

    def __str__(self):
        try:
            return u"%s" % (self.person)
        except Person.DoesNotExist:
            # if it is not a person it must be an organization
            return u"%s" % (self.organization)


@python_2_unicode_compatible
class Person(Actor):
    redmine_contact_id = models.IntegerField(
        verbose_name=_("Redmine contact"),
        null=True,
        blank=True
    )

    first_name = models.CharField(
        verbose_name=_("First name"),
        max_length=30
    )

    family_name = models.CharField(
        verbose_name=_("Family name"),
        max_length=50,
        null=True,
        blank=True
    )

    phone = models.CharField(
        verbose_name=_("Phone"),
        max_length=30,
        null=True,
        blank=True
    )

    street_number = models.CharField(
        verbose_name=_("Number"),
        max_length=10,
        null=True,
        blank=True
    )

    street = models.CharField(
        verbose_name=_("Street"),
        max_length=50,
        null=True,
        blank=True
    )

    complement = models.CharField(
        verbose_name=_("Complement"),
        max_length=150,
        null=True,
        blank=True
    )

    postal_code = models.CharField(
        verbose_name=_("Postal code"),
        max_length=10,
        null=True,
        blank=True
    )

    neighborhood = models.ForeignKey(
        'Neighborhood',
        verbose_name=_("Neighborhood"),
        null=True,
    )

    city = models.ForeignKey(
        'City',
        verbose_name=_("City"),
        null=True,
        default=1
    )

    state = models.ForeignKey(
        'State',
        verbose_name=_("State"),
        null=True,
        default=1
    )

    country = models.ForeignKey(
        'Country',
        verbose_name=_("Country"),
        null=True,
        default=1
    )

    longitude = models.FloatField(
        verbose_name=_("Longitude"),
        null=True,
        blank=True
    )

    latitude = models.FloatField(
        verbose_name=_("Latitude"),
        null=True,
        blank=True
    )

    language = models.ForeignKey(
        'member.Language',
        null=True,
        blank=True,
        verbose_name=_("Preferred language")
    )

    comments = models.TextField(
        verbose_name=_("Comments"),
        blank=True
    )

    class Meta:
        verbose_name = _("person")
        verbose_name_plural = _("people")

    def __str__(self):
        return u"%s %s" % (self.first_name, self.family_name)

    def name(self):
        return u"%s %s" % (self.first_name, self.family_name)

    def email(self):
        auth_obj = AuthUser.objects.get(person=self)
        return auth_obj.email

    def participation_count(self):
        count = RequestForParticipation.objects.filter(picker=self, is_accepted=True).count()
        return count

@python_2_unicode_compatible
class Organization(Actor):
    is_beneficiary = models.BooleanField(
        verbose_name=_('is beneficiary'),
        default=False
    )

    redmine_contact_id = models.IntegerField(
        verbose_name=_("Redmine contact"),
        null=True,
        blank=True
    )

    civil_name = models.CharField(
        verbose_name=_("Name"),
        max_length=50
    )

    description = models.TextField(
        verbose_name=_("Description"),
        blank=True
    )

    phone = models.CharField(
        verbose_name=_("Phone"),
        max_length=50,
        null=True
    )

    contact_person = models.ForeignKey(
        'Person',
        null=True,
        verbose_name=_("Contact person")
    )

    contact_person_role = models.CharField(
        verbose_name=_("Contact person role"),
        max_length=50,
        null=True,
        blank=True
    )

    street_number = models.CharField(
        verbose_name=_("Number"),
        max_length=10,
        null=True,
        blank=True
    )

    street = models.CharField(
        verbose_name=_("Street"),
        max_length=50,
        null=True,
        blank=True
    )

    complement = models.CharField(
        verbose_name=_("Complement"),
        max_length=150,
        null=True,
        blank=True
    )

    postal_code = models.CharField(
        verbose_name=_("Postal code"),
        max_length=10,
        null=True,
        blank=True
    )

    neighborhood = models.ForeignKey(
        'Neighborhood',
        verbose_name=_("Neighborhood"),
        null=True,
    )

    city = models.ForeignKey(
        'City',
        verbose_name=_("City"),
        null=True,
        default=1
    )

    state = models.ForeignKey(
        'State',
        verbose_name=_("State"),
        null=True,
        default=1
    )

    country = models.ForeignKey(
        'Country',
        verbose_name=_("Country"),
        null=True,
        default=1
    )

    longitude = models.FloatField(
        verbose_name=_("Longitude"),
        null=True,
        blank=True
    )

    latitude = models.FloatField(
        verbose_name=_("Latitude"),
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = _("organization")
        verbose_name_plural = _("organizations")

    def __str__(self):
        return u"%s" % self.civil_name

    def name(self):
        return u"%s" % self.civil_name


@python_2_unicode_compatible
class Neighborhood(models.Model):
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=150
    )

    class Meta:
        verbose_name = _("neighborhood")
        verbose_name_plural = _("neighborhoods")

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class City(models.Model):
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=150
    )

    class Meta:
        verbose_name = _("city")
        verbose_name_plural = _("cities")

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class State(models.Model):
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=150
    )

    class Meta:
        verbose_name = _("states")

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Country(models.Model):
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=150
    )

    class Meta:
        verbose_name = _("country")
        verbose_name_plural = _("countries")

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Language(models.Model):
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=150
    )

    class Meta:
        verbose_name = _("language")
        verbose_name_plural = _("languages")

    def __str__(self):
        return self.name

