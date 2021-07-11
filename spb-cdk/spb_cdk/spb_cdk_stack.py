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