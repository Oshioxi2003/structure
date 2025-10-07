"""
Seed demo data for development
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.users.models import User


def seed_users():
    """Create demo users"""
    print("Creating demo users...")
    
    # Create admin user
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin123',
            first_name='Admin',
            last_name='User'
        )
        print("✓ Admin user created")
    
    # Create demo users
    demo_users = [
        {
            'username': 'john_doe',
            'email': 'john@example.com',
            'password': 'password123',
            'first_name': 'John',
            'last_name': 'Doe',
        },
        {
            'username': 'jane_smith',
            'email': 'jane@example.com',
            'password': 'password123',
            'first_name': 'Jane',
            'last_name': 'Smith',
        },
    ]
    
    for user_data in demo_users:
        if not User.objects.filter(username=user_data['username']).exists():
            password = user_data.pop('password')
            user = User(**user_data)
            user.set_password(password)
            user.save()
            print(f"✓ User {user.username} created")


def run():
    """Run all seed functions"""
    print("Seeding demo data...")
    seed_users()
    print("Demo data seeded successfully!")


if __name__ == "__main__":
    run()
