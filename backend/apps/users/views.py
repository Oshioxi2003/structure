"""
User views
"""
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import User
from .serializers import UserSerializer, UserCreateSerializer, UserUpdateSerializer
from . import selectors, services
from apps.common.exceptions import BusinessLogicError


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for User model
    
    list: Get all users
    retrieve: Get user by ID
    create: Create new user
    update: Update user
    partial_update: Partial update user
    destroy: Delete user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return UserUpdateSerializer
        return UserSerializer
    
    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAuthenticated()]
    
    @action(detail=False, methods=['get'])
    def me(self, request):
        """Get current user profile"""
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
    
    @action(detail=False, methods=['put'])
    def update_profile(self, request):
        """Update current user profile"""
        try:
            user = services.update_user(request.user, request.data)
            serializer = self.get_serializer(user)
            return Response(serializer.data)
        except BusinessLogicError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['post'])
    def change_password(self, request):
        """Change user password"""
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        
        if not old_password or not new_password:
            return Response(
                {'error': 'Both old and new passwords are required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            services.change_password(request.user, old_password, new_password)
            return Response({'message': 'Password changed successfully'})
        except BusinessLogicError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['get'])
    def search(self, request):
        """Search users"""
        query = request.query_params.get('q', '')
        users = selectors.search_users(query)
        
        page = self.paginate_queryset(users)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)
