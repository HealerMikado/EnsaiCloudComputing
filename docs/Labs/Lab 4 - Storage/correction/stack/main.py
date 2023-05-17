from constructs import Construct
from cdktf import App, TerraformStack
from cdktf_cdktf_provider_aws.provider import AwsProvider
from cdktf_cdktf_provider_aws.dynamodb_table import DynamodbTable, DynamodbTableAttribute, DynamodbTableGlobalSecondaryIndex

class DynamoDBStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        AwsProvider(self, "AWS", region="us-east-1")

        bucket = DynamodbTable(
            self, "DynamodDB-table",
            name= "battle-royal",
            hash_key="PK",
            range_key="SK",
            attribute=[
                DynamodbTableAttribute(name="PK",type="S" ),
                DynamodbTableAttribute(name="SK",type="S" )
            ],
            global_secondary_index=[
                DynamodbTableGlobalSecondaryIndex(
                    name="InvertedIndex",
                    hash_key="SK",
                    range_key="PK",
                    projection_type="ALL",
                    write_capacity=5,
                    read_capacity=5

                )
            ],
            billing_mode="PROVISIONED",
            read_capacity=5,
            write_capacity=5
        )

app = App()
DynamoDBStack(app, "DynamoDBStack")
app.synth()