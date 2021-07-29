import os
from aws_cdk import core as cdk
from cdk_spb.cdk_spb_stack import CdkSpbStack

app = cdk.App()
CdkSpbStack(app, "CdkSpbStack",
    )

app.synth()
