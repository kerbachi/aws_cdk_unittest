# Simple CDK project with Python demonstrating:

* Unit test with aws_cdk.assertions
* Doc to export package to PyPi

## Without supression these ERROR will stop the deployment

```
(.venv) ➜  aws_cdk_helloworld git:(master) ✗ cdk synth
[Error at /AwsCdkHelloworldStack/AwsCdkHelloworldQueue/Resource] AwsSolutions-SQS3: The SQS queue is not used as a dead-letter queue (DLQ) and does not have a DLQ enabled.

[Error at /AwsCdkHelloworldStack/AwsCdkHelloworldQueue/Resource] AwsSolutions-SQS4: The SQS queue does not require requests to use SSL.


Found errors
```

# CDK NAG rules

https://github.com/cdklabs/cdk-nag/blob/HEAD/RULES.md#additional-rules



# PyPi packaging

To create an AWS CDK construct as a Pip package, follow these steps:

1. Choose a programming language: AWS CDK supports Python, JavaScript (TypeScript), and Java. For this example, we’ll use Python.
2. Create a new directory for your construct package. Initialize a new Python package using pip:

```
mkdir my_cdk_construct
cd my_cdk_construct
python -m pip init
```

3. *Install AWS CDK for Python* as a development dependency:
```
python -m pip install -r requirements.txt aws-cdk
```

4. Create a new construct class in a file named __init__.py (or construct.py if you prefer). This class should extend aws_cdk.core.Construct. For example:

```
from aws_cdk import core

class MyCdkConstruct(core.Construct):
    def __init__(self, scope: core.Construct, id: str, **props):
        super().__init__(scope, id, props)
        # Define your construct's logic and resources here
```

5. Define your construct’s resources and logic within the MyCdkConstruct class. This might include creating AWS resources, such as S3 buckets or Lambda functions, using AWS CDK’s API.

6. Create a setup.py file to define your package’s metadata and dependencies:

```
from setuptools import setup

setup(
    name='my_cdk_construct',
    version='1.0.0',
    packages=['my_cdk_construct'],
    install_requires=['aws-cdk'],
    author='Your Name',
    author_email='your.email@example.com'
)
```

7. Build and package your construct using setuptools:
```
python setup.py sdist bdist_wheel
```

8. Upload your package to PyPI using twine:
```
twine upload dist/*
```

9. Install your package using Pip:
```
pip install my_cdk_construct
```

My package:
https://pypi.org/project/aws-cdk-helloworld/



# Deployment

This is a blank project for CDK development with Python.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation


# Unit test


```
(.venv) ➜ ✗ pytest
================================================================= test session starts ==================================================================
platform darwin -- Python 3.12.2, pytest-8.3.3, pluggy-1.5.0
rootdir: /Users/me/Documents/code/aws_cdk_helloworld
plugins: typeguard-2.13.3
collected 2 items                                                                                                                                      

tests/cdk_test.py .                                                                                                                              [ 50%]
tests/unit/test_aws_cdk_helloworld_stack.py .                                                                                                    [100%]

================================================================== 2 passed in 2.74s ===================================================================
(.venv) ➜  ✗ 
```

Enjoy!
