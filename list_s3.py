import boto3 # type: ignore

# Initialize the AWS client

s3 = boto3.client('s3')


# Lisst S3 buckets

response = s3.list_buckets()
print("S3 buckets: ")
for bucket in response['Buckets']:
    print(f'- {bucket["Name"]}')