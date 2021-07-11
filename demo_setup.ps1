python -m ensurepip --upgrade
python -m pip install --upgrade pip
python -m pip install --upgrade virtualenv
pip install aws-cdk.aws_apigateway

pip install aws-cdk.aws-s3
pip install aws-cdk.aws-lambda
pip install aws-cdk.aws_apigateway

md spb-cdk
cd spb-cdk
md lambda

cdk init --language python
	python -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt

# spb_cdk\spb_cdk_stack.py
<#
from aws_cdk import (
    # aws_iam as iam,
    aws_apigateway as apigw,
    aws_lambda as _lambda,
    aws_s3 as s3,
    core as cdk,
    core,
)

class SpbCdkStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(self, 
            "Bag-O", 
            versioned=False,
            removal_policy=core.RemovalPolicy.DESTROY,
#            auto_delete_objects=True
          )

        spb_lambda =_lambda.Function(
            self, 'SPB_HelloHandle',
            runtime=_lambda.Runtime.PYTHON_3_8,
            code=_lambda.Code.asset('lambda'),
            #code=_lambda.Code.from_bucket(bucket)
            handler='sbp.handler'
        )

#        apigw.LambdaRestApi(
#            self, 'Endpoint',
#            handler=spb_lambda,
#        )
#>

# lambda\hello.py
<# 
import json


def handler(event, context):
    print('request: {}'.format(json.dumps(event)))
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': 'Hello, CDK! You have hit {}\n'.format(event['path'])
    }
#>