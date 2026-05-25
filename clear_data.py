import os
import django
import boto3

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_site.settings')
django.setup()

from django.conf import settings
from core.models import Todo

print("Clearing database...")
Todo.objects.all().delete()
print("Database cleared!")

print("Clearing S3 Bucket...")
s3 = boto3.resource(
    's3',
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    region_name=settings.AWS_S3_REGION_NAME
)
bucket = s3.Bucket(settings.AWS_STORAGE_BUCKET_NAME)
bucket.objects.all().delete()
print("S3 Bucket cleared!")
