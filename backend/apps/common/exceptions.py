"""
Custom exceptions
"""
from rest_framework.exceptions import APIException
from rest_framework import status


class BusinessLogicError(APIException):
    """Base exception for business logic errors"""
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'A business logic error occurred.'
    default_code = 'business_error'


class ResourceNotFoundError(APIException):
    """Exception when resource is not found"""
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = 'Resource not found.'
    default_code = 'not_found'


class PermissionDeniedError(APIException):
    """Exception when permission is denied"""
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = 'You do not have permission to perform this action.'
    default_code = 'permission_denied'
