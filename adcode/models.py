"Models for managing site sections and ad placements."

from django.db import models


class Section(models.Model):
    "A grouping of site urls."

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    pattern = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Size(models.Model):
    "Common Ad size."

    name = models.CharField(max_length=100)
    width = models.PositiveSmallIntegerField()
    height = models.PositiveSmallIntegerField()

    def __unicode__(self):
        return u'{0} ({1}x{2})'.format(self.name, self.width, self.height)


class Placement(models.Model):
    "Ad to be rendered in given sections."

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    size = models.ForeignKey(Size, related_name='placements')
    sections = models.ManyToManyField(Section, related_name='placements')

    def __unicode__(self):
        return u'{0} ({1})'.format(self.name, self.size)
