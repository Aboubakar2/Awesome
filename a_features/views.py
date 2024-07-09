from django.shortcuts import render
from django.conf import settings

from a_features.models import Feature


def feature_enable(pk, developer):
    feature = Feature.objects.get(id=pk)
    if (settings.ENVIRONMENT == 'development' and settings.DEVELOPER == developer) or \
            (feature.staging_enabled and settings.STAGING) or feature.production_enabled:
        feature_enabled = True
    else:
        feature_enabled = False
    return feature_enabled
