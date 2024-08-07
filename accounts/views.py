import json
from functools import reduce

from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from django_rest_passwordreset.models import ResetPasswordToken
from rest_framework import filters, mixins, status, viewsets
from rest_framework.filters import BaseFilterBackend
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import User
from accounts.serializers import UserSerializer, UserSerializerPost


class UserViewset(mixins.ListModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):

    permission_classes = (AllowAny,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id', 'email', 'first_name', 'last_name', 
                     'date_joined',  'first_login',  'is_active',  'is_admin')
    
    def get_serializer_class(self):
        if self.action == 'create':
            return UserSerializerPost
        else:
            return UserSerializer
        
    def get_queryset(self):
        queryset = User.objects.all()
                
        return queryset


class GetUserKeyPassword(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        data = json.loads(request.body)

        key = data.get('key')
        result = {}
        if key is not None:
            try:
                result['email'] = ResetPasswordToken.objects.get(key=key).user.email
                status_result = status.HTTP_200_OK

            except ResetPasswordToken.DoesNotExist:
                result['message'] = 'This key is not related to any user.'
                status_result = status.HTTP_400_BAD_REQUEST
        else:
            result['message'] = 'The "key" argument is required.'
            status_result = status.HTTP_400_BAD_REQUEST


        return Response(result, status=status_result)