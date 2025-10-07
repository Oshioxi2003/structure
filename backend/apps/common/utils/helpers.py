"""
Common utility functions
"""
from datetime import datetime
from typing import Optional


def generate_unique_filename(filename: str, prefix: Optional[str] = None) -> str:
    """
    Generate a unique filename with timestamp
    
    Args:
        filename: Original filename
        prefix: Optional prefix
        
    Returns:
        Unique filename
    """
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    name_parts = filename.rsplit('.', 1)
    
    if len(name_parts) == 2:
        name, ext = name_parts
        if prefix:
            return f"{prefix}_{timestamp}_{name}.{ext}"
        return f"{timestamp}_{name}.{ext}"
    
    if prefix:
        return f"{prefix}_{timestamp}_{filename}"
    return f"{timestamp}_{filename}"


def format_phone_number(phone: str) -> str:
    """
    Format phone number to standard format
    
    Args:
        phone: Phone number string
        
    Returns:
        Formatted phone number
    """
    # Remove all non-digit characters
    digits = ''.join(filter(str.isdigit, phone))
    
    # Format as Vietnamese phone number
    if len(digits) == 10:
        return f"+84{digits[1:]}"
    elif len(digits) == 11 and digits.startswith('84'):
        return f"+{digits}"
    
    return phone
