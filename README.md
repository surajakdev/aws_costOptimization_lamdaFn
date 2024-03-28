# aws_costOptimization_lamdaFn

## Cost Optimization using aws lambda function and boto3 python module.
### This python lambda function is to check and delete if there is any stale snapshot ( snapshot which was created by developer for backup of ec2's volume)  if it is not attached to any instance or if the instance along with volume is terminated in that case snapshot will be removed by this python lambda function.

### Here in this case lambda function needs to be executed manually. If it needs to be executed automatically at a specified time then the cronjob sceduling need to be used in cloudwatch of aws.

### Here the boto3 module of python for interacting with apis of aws is used.

## Take branch named branch1 for python code.
