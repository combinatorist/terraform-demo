import os
from datetime import datetime, timezone

import boto3

s3 = boto3.resource('s3')
s3_object = s3.Object(os.environ['S3_BUCKET'], os.environ['S3_KEY'])

def last_modified(event, context):
    """
    Initializes of overwrites s3 file with current time as 'last modified' text
    """
    body = ('Last Modified @ ' +  datetime.now(timezone.utc).isoformat()).encode()
    return s3_object.put(Body=body, ACL='public-read', ContentType='text/html',
        StorageClass='REDUCED_REDUNDANCY')
