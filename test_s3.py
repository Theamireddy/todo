import os
import django
from dotenv import load_dotenv

load_dotenv()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_site.settings')
django.setup()

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

try:
    print("Bucket:", os.getenv('AWS_STORAGE_BUCKET_NAME'))
    print("Region:", os.getenv('AWS_S3_REGION_NAME'))
    path = default_storage.save('test.txt', ContentFile(b'new content'))
    print("Saved file to:", path)
    
except Exception as e:
    import traceback
    traceback.print_exc()
