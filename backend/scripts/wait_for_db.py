"""
Wait for database to be ready before running migrations
"""
import time
import sys
import psycopg2
from psycopg2 import OperationalError


def wait_for_db(max_retries=30, delay=1):
    """
    Wait for database to be available
    
    Args:
        max_retries: Maximum number of retries
        delay: Delay between retries in seconds
    """
    print("Waiting for database...")
    
    retries = 0
    while retries < max_retries:
        try:
            conn = psycopg2.connect(
                dbname="edu_db",
                user="postgres",
                password="postgres",
                host="localhost",
                port="5432"
            )
            conn.close()
            print("Database is ready!")
            return True
        except OperationalError:
            retries += 1
            print(f"Database unavailable, waiting... ({retries}/{max_retries})")
            time.sleep(delay)
    
    print("Could not connect to database")
    sys.exit(1)


if __name__ == "__main__":
    wait_for_db()
