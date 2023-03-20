# Un instance base

from constructs import Construct
from cdktf import App, TerraformStack, TerraformOutput
from cdktf_cdktf_provider_aws.provider import AwsProvider
from cdktf_cdktf_provider_aws.instance import Instance, InstanceEbsBlockDevice
from cdktf_cdktf_provider_aws.security_group import SecurityGroup, SecurityGroupIngress, SecurityGroupEgress
from user_data import user_data

class MyStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        AwsProvider(self, "AWS", region="us-east-1")
        TerraformOutput(
            self, "public_ip",
            value=instance.public_ip,
            )


app = App()
MyStack(app, "cloud_commputing")

app.synth()


# Configuration de la partie réseau

security_group = SecurityGroup(
    self, "sg-tp",
    ingress=[
        SecurityGroupIngress(
            from_port=22,
            to_port=22,
            cidr_blocks=["0.0.0.0/0"],
            protocol="TCP",
            description="Accept incoming SSH connection"
        ),
        SecurityGroupIngress(
            from_port=80,
            to_port=80,
            cidr_blocks=["0.0.0.0/0"],
            protocol="TCP",
            description="Accept incoming HTTP connection"
        )
    ],
    egress=[
        SecurityGroupEgress(
            from_port=0,
            to_port=0,
            cidr_blocks=["0.0.0.0/0"],
            protocol="-1",
            description="allow all egresse connection"
        )
    ]
)

# Configuration des disques (bonus)

ebs_block_device= [InstanceEbsBlockDevice(
    device_name="/dev/sda1",
    delete_on_termination=True,
    encrypted=False,
    volume_size=20,
    volume_type="gp2"
),
InstanceEbsBlockDevice(
    device_name="/dev/sdb",
    delete_on_termination=True,
    encrypted=False,
    volume_size=100,
    volume_type="gp2"
)]

