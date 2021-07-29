from aws_cdk import aws_apigateway as apigw
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_s3 as s3
from aws_cdk import core as cdk


class CdkSpbStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # bucket = s3.Bucket(self, 
        #     "MyFirstBucket", 
        #     versioned=True,
        #     removal_policy=cdk.RemovalPolicy.DESTROY,
        #     auto_delete_objects=True)

        # Defines an AWS Lambda resource
        my_lambda = _lambda.Function(
            self, 'Hello, hello',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.asset('lambda'),
            handler='hello.handler',
        )

        apigw.LambdaRestApi(
            self, 'Endpoint',
            handler=my_lambda,
        )