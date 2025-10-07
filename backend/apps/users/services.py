"""
User services - Business logic for write operations
"""
from typing import Dict, Any
from django.db import transaction
from .models import User
from apps.common.exceptions import BusinessLogicError


@transaction.atomic
def create_user(data: Dict[str, Any]) -> User:
    """
    Create a new user
    
    Args:
        data: User data
        
    Returns:
        Created user instance
        
    Raises:
        BusinessLogicError: If user creation fails
    """
    email = data.get('email')
    username = data.get('username')
    
    # Check if email already exists
    if User.objects.filter(email=email).exists():
        raise BusinessLogicError('Email already exists')
    
    # Check if username already exists
    if User.objects.filter(username=username).exists():
        raise BusinessLogicError('Username already exists')
    
    password = data.pop('password')
    user = User(**data)
    user.set_password(password)
    user.save()
    
    return user


@transaction.atomic
def update_user(user: User, data: Dict[str, Any]) -> User:
    """
    Update user profile
    
    Args:
        user: User instance to update
        data: Update data
        
    Returns:
        Updated user instance
    """
    for key, value in data.items():
        if hasattr(user, key):
            setattr(user, key, value)
    
    user.save()
    return user


@transaction.atomic
def change_password(user: User, old_password: str, new_password: str) -> User:
    """
    Change user password
    
    Args:
        user: User instance
        old_password: Current password
        new_password: New password
        
    Returns:
        Updated user instance
        
    Raises:
        BusinessLogicError: If old password is incorrect
    """
    if not user.check_password(old_password):
        raise BusinessLogicError('Current password is incorrect')
    
    user.set_password(new_password)
    user.save()
    
    return user


@transaction.atomic
def verify_user(user: User) -> User:
    """
    Verify user account
    
    Args:
        user: User instance
        
    Returns:
        Verified user instance
    """
    user.is_verified = True
    user.save()
    return user
