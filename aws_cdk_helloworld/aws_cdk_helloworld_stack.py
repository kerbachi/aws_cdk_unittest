from aws_cdk import (
    Duration,
    Stack,
    aws_iam,
    Aws,
    aws_sqs as sqs
)
from constructs import Construct
from cdk_nag import NagSuppressions

class AwsCdkHelloworldStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource (SQS)
        queue = sqs.Queue(
            self, "AwsCdkHelloworldQueue",
            visibility_timeout=Duration.seconds(300),
        )

        # IAM Permissions
        role = aws_iam.Role(self, 
                            "EC2Role",
                            role_name="EC2Role4SQS",
                            assumed_by=aws_iam.CompositePrincipal(
                                aws_iam.ServicePrincipal("ec2.amazonaws.com")
                                # aws_iam.AccountPrincipal(Aws.ACCOUNT_ID)
                            ))

        role.add_to_policy(aws_iam.PolicyStatement(
            sid="QueueSendPermission",
            resources=[queue.queue_arn],
            effect=aws_iam.Effect.ALLOW,
            actions=["sqs:SendMessage"]
        ))


        # Supressions
        NagSuppressions.add_resource_suppressions(queue, 
                                                  [
                                                      { 
                                                          "id": "AwsSolutions-SQS3", 
                                                          "reason": "No need for DLQ for this demo" 
                                                       },
                                                      { 
                                                          "id": "AwsSolutions-SQS4", 
                                                          "reason": "No need for SSL for this demo" 
                                                       }
                                                  ]
                                                  )


