#!/usr/bin/env python3
import os

import aws_cdk as cdk
import cdk_nag
from aws_cdk_helloworld.aws_cdk_helloworld_stack import AwsCdkHelloworldStack
from aws_cdk import assertions as assertions



app = cdk.App()
AwsCdkHelloworldStack(app, "AwsCdkHelloworldStack",
    # If you don't specify 'env', this stack will be environment-agnostic.
    # Account/Region-dependent features and context lookups will not work,
    # but a single synthesized template can be deployed anywhere.

    # Uncomment the next line to specialize this stack for the AWS Account
    # and Region that are implied by the current CLI configuration.

    #env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),

    # Uncomment the next line if you know exactly what Account and Region you
    # want to deploy the stack to. */

    #env=cdk.Environment(account='123456789012', region='us-east-1'),

    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
    )

cdk.Aspects.of(app).add(cdk_nag.AwsSolutionsChecks())

app.synth()


# create test unit with AwsCdkHelloworldStack





# def test_stack():
#     testing_stack = AwsCdkHelloworldStack(scope=cdk.App(), id='TestStack')
#     # synthesized_stack = testing_stack.to_json()
#     # assert assertions.Template(
#     #     synthesized_stack,
#     #     has_resource('AWS::SQS::Queue')
#     # )
#     template = template.from_stack(testing_stack)
#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })

#     # app = core.App()
#     # stack = AwsCdkHelloworldStack(app, "test")
#     # template = assertions.Template.from_stack(stack)

#     # template.has_resource_properties("AWS::SQS::Queue", {
#     #     "VisibilityTimeout": 300
#     # })
