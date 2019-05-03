from json import dumps
from boto3 import client, session
from requests import get
from os import environ
from logging import getLogger, info

BUCKET = environ['BUCKET_NAME']
KEY = environ['KEY']


def lambda_handler(event, context):

    client_s3 = client('s3', config=session.Config(signature_version='s3v4'))
    logger = getLogger()
    logger.setLevel("INFO")

    # Generate the URL to get 'key-name' from 'bucket-name'
    url = client_s3.generate_presigned_url(
        ClientMethod='get_object',
        Params={
            'Bucket': BUCKET,
            'Key': KEY
        },
        ExpiresIn=60*10
    )

    response = get(url)
    info(KEY)
    info(response)
    info(url)
