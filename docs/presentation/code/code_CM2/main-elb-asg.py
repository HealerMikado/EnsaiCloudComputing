#!/usr/bin/env python
from constructs import Construct
from cdktf import App, NamedRemoteWorkspace, TerraformStack, TerraformOutput, RemoteBackend
from cdktf_cdktf_provider_aws.provider import AwsProvider
from cdktf_cdktf_provider_aws.launch_template import LaunchTemplate
from cdktf_cdktf_provider_aws.lb import Lb
from cdktf_cdktf_provider_aws.lb_target_group import LbTargetGroup
from cdktf_cdktf_provider_aws.lb_listener import LbListener, LbListenerDefaultAction
from cdktf_cdktf_provider_aws.autoscaling_attachment import AutoscalingAttachment
from cdktf_cdktf_provider_aws.autoscaling_group import AutoscalingGroup, AutoscalingGroupLaunchTemplate
from cdktf_cdktf_provider_aws.security_group import SecurityGroup, SecurityGroupIngress, SecurityGroupEgress
from user_data import user_data

class MyStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        AwsProvider(self, "AWS", region="us-east-1")

        security_group = SecurityGroup(
            self, "sg-tp",
            ingress=[
                SecurityGroupIngress(
                    from_port=22,
                    to_port=22,
                    cidr_blocks=["0.0.0.0/0"],
                    protocol="TCP",
                ),
                SecurityGroupIngress(
                    from_port=80,
                    to_port=80,
                    cidr_blocks=["0.0.0.0/0"],
                    protocol="TCP"
                )
            ],
            egress=[
                SecurityGroupEgress(
                    from_port=0,
                    to_port=0,
                    cidr_blocks=["0.0.0.0/0"],
                    protocol="-1"
                )
            ]
            )

        launch_template = LaunchTemplate(
            self, "compute",
            image_id="ami-0557a15b87f6559cf",
            instance_type="t2.micro",
            user_data=user_data,
            vpc_security_group_ids=[security_group.id],
            key_name="vockey"
            )
        
        target_group = LbTargetGroup(
            self, "target_group",
            port=80,
            protocol="HTTP",
            vpc_id="vpc-08e79f3175b582837"
        )
        
        elb = Lb(
            self, "ELB",
            load_balancer_type="application",
            subnets=["subnet-0f52ad57bf37522f3", "subnet-0d7dd9609fe9ed2ce"],
            security_groups=[security_group.id]
        )

        lb_listener = LbListener(
            self, "lb_listener",
            load_balancer_arn=elb.arn,
            port=80,
            protocol="HTTP",
            default_action=[LbListenerDefaultAction(
                type="forward",
                target_group_arn=target_group.arn
            )]
            # default_action=[{"target_group_arn":target_group.arn, "type": "forward",}]

        )

        asg = AutoscalingGroup(
            self,
            "asg",
            min_size=2,
            desired_capacity=3,
            max_size=4,
            launch_template=AutoscalingGroupLaunchTemplate(id=launch_template.id),
            vpc_zone_identifier=["subnet-0f52ad57bf37522f3", "subnet-0d7dd9609fe9ed2ce"],
            target_group_arns=[target_group.arn]
        )

        


app = App()
MyStack(app, "cloud_commputing")

app.synth()
