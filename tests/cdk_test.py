from aws_cdk import assertions as assertions
import aws_cdk as cdk
from app import AwsCdkHelloworldStack

def test_stack():
    app = cdk.App()
    testing_stack = AwsCdkHelloworldStack(app, "TestStack")

    template = assertions.Template.from_stack(testing_stack)

    template.has_resource_properties("AWS::SQS::Queue", {
        "VisibilityTimeout": 300
    })
