import requests
import datetime
from django.db.models import Sum

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny

from django.shortcuts import get_object_or_404

