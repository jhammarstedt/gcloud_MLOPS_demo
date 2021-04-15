import argparse
import datetime
import logging
import os
import mnist

from google.cloud import storage

# credentials_dict = {
#     'type': 'service_account',
#     'client_id': os.environ['BACKUP_CLIENT_ID'],
#     'client_email': os.environ['BACKUP_CLIENT_EMAIL'],
#     'private_key_id': os.environ['BACKUP_PRIVATE_KEY_ID'],
#     'private_key': os.environ['BACKUP_PRIVATE_KEY'],
# }

def preprocess(PROJECT, BUCKET):
    print("test preprocess")
    OUTPUT_DIR = 'gs://{0}/mnist/'.format(BUCKET)

    storage_client = storage.Client(project=PROJECT)

    bucket = storage_client.bucket('mnist')
    new_bucket = storage_client.create_bucket(bucket)
    print(
        "Created bucket {} in {} with storage class {}".format(
            new_bucket.name, new_bucket.location, new_bucket.storage_class
        )
    )


if __name__ == '__main__':
  logging.getLogger().setLevel(logging.INFO)
  parser = argparse.ArgumentParser()
  parser.add_argument('--project',
                      type=str,
                      required=True,
                      help='The GCP project to run the dataflow job.')
  parser.add_argument('--bucket',
                      type=str,
                      required=True,
                      help='Bucket to store outputs.')
  parser.add_argument('--mode',
                      choices=['local', 'cloud'],
                      help='whether to run the job locally or in Cloud Dataflow.')

  args = parser.parse_args()

  preprocess(args.project, args.bucket)