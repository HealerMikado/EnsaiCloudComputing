#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack
from cdktf_cdktf_provider_aws.provider import AwsProvider
from cdktf_cdktf_provider_aws.dynamodb_table import DynamodbTable, DynamodbTableAttribute

class DynamoDBStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        AwsProvider(self, "AWS", region="us-east-1")

        bucket = DynamodbTable(
            self, "DynamodDB-table",
            name= "user_score",
            hash_key="username",
            range_key="lastename",
            attribute=[
                DynamodbTableAttribute(name="username",type="S" ),
                DynamodbTableAttribute(name="lastename",type="S" )
            ],
            billing_mode="PROVISIONED",
            read_capacity=5,
            write_capacity=5

        )

app = App()
DynamoDBStack(app, "DynamoDBStack")

app.synth()
