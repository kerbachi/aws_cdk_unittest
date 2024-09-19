import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_cdk_helloworld.aws_cdk_helloworld_stack import AwsCdkHelloworldStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_cdk_helloworld/aws_cdk_helloworld_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsCdkHelloworldStack(app, "aws-cdk-helloworld")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
