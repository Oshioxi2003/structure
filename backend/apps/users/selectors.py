"""
User selectors - Read-only database queries
"""
from typing import Optional
from django.db.models import QuerySet
from .models import User


def get_user_by_id(user_id: int) -> Optional[User]:
    """
    Get user by ID
    
    Args:
        user_id: User ID
        
    Returns:
        User instance or None
    """
    try:
        return User.objects.get(id=user_id)
    except User.DoesNotExist:
        return None


def get_user_by_email(email: str) -> Optional[User]:
    """
    Get user by email
    
    Args:
        email: User email
        
    Returns:
        User instance or None
    """
    try:
        return User.objects.get(email=email)
    except User.DoesNotExist:
        return None


def get_all_users(is_active: Optional[bool] = None) -> QuerySet[User]:
    """
    Get all users with optional filtering
    
    Args:
        is_active: Filter by active status
        
    Returns:
        QuerySet of users
    """
    queryset = User.objects.all()
    
    if is_active is not None:
        queryset = queryset.filter(is_active=is_active)
    
    return queryset


def search_users(query: str) -> QuerySet[User]:
    """
    Search users by username, email, or name
    
    Args:
        query: Search query
        
    Returns:
        QuerySet of matching users
    """
    return User.objects.filter(
        username__icontains=query
    ) | User.objects.filter(
        email__icontains=query
    ) | User.objects.filter(
        first_name__icontains=query
    ) | User.objects.filter(
        last_name__icontains=query
    )
