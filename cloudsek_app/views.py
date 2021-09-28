from django.shortcuts import render
import json
from django.http import Http404
from django.views import View
from cloudsek_app.serializers import AmountSerializer, AmountResultSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from cloudsek_app.constants import ID, ID_PK, TOTAL, MESSAGE
from cloudsek_app.db_handler import build_payload_and_calculate
from cloudsek_app.validation import CustomValidation
from cloudsek_app.models import Amount

# Create your views here.
class AmountView(APIView):
    
    def __init__(self):
        self.custome_validation = CustomValidation()

    def get(self, request):
        return Response({MESSAGE}, status=status.HTTP_200_OK)


    def post(self, request):
        try:
            self.custome_validation.get_and_validate(request.data)
            payload = build_payload_and_calculate(self, request.data)
            serializer = AmountSerializer(data=payload)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({ID: payload.get(ID_PK)}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(status=status.HTTP_204_NO_CONTENT)


class ResultView(APIView):

    def get(self, request, uuid):
        try:
            user = Amount.objects.get(id_pk=uuid)
            serializer = AmountResultSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND)