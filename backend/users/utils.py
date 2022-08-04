import uuid


def hash_upload(instance, filename):
    filename = str(uuid.uuid4())[:8] + "-" + filename
    return f"profile_photos/{filename}"
