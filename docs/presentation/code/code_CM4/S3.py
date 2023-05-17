#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack
from cdktf_cdktf_provider_aws.provider import AwsProvider
from cdktf_cdktf_provider_aws.s3_bucket import S3Bucket

class S3Stack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        AwsProvider(self, "AWS", region="us-east-1")

        bucket = S3Bucket(
            self, "s3_bucket",
            bucket = "my-cdtf-test-bucket-20230321",
            acl="private",
            force_destroy=True
        )

app = App()
S3Stack(app, "S3")

app.synth()
