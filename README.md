# AWS Cost Optimization Lambda function.

## Cost Optimization using AWS lambda function and boto3 python module.
### This python lambda function is to check and delete if there is any stale snapshot ( snapshot which was created by developer for backup of ec2's volume)  if it is not attached to any instance or if the instance along with volume is terminated in that case snapshot will be removed by this python lambda function.

### Here in this case lambda function needs to be executed manually. If it needs to be executed automatically at a specified time then the cronjob sceduling need to be used in cloudwatch of aws.

### Here the boto3 module of python for interacting with apis of aws is used.

## Take branch named branch1 for python code.

### Creating instance.
![1](https://github.com/surajakdev/aws_costOptimization_lamdaFn/assets/158173648/4b13ab2f-273f-4217-9313-7be4f47a9eb6)


### Creating snapshot of specified volume for backup puprose.

![8](https://github.com/surajakdev/aws_costOptimization_lamdaFn/assets/158173648/29023b7d-1ead-41e8-9497-36193a58ec50)

![9](https://github.com/surajakdev/aws_costOptimization_lamdaFn/assets/158173648/85cc6c05-7310-4de3-a016-e68de681f689)

### Creating Lambda function containing python code.
![12](https://github.com/surajakdev/aws_costOptimization_lamdaFn/assets/158173648/8671b40d-804b-46f6-8061-271540e16237)

### Assigning execution role permission to lambda function 
#### Permission such as snapshot listing and to delete.

![19](https://github.com/surajakdev/aws_costOptimization_lamdaFn/assets/158173648/c804904f-5761-44de-bd49-08425d26c267)

#### Permission to list insatnces and volume.
![27](https://github.com/surajakdev/aws_costOptimization_lamdaFn/assets/158173648/ef1865a4-affe-4b5a-b8b1-08dc5597187f)

### Policy created.
![22](https://github.com/surajakdev/aws_costOptimization_lamdaFn/assets/158173648/8685dec4-1553-4a4c-94f6-70fff18227cd)

### Search and add newly created policy.
![25](https://github.com/surajakdev/aws_costOptimization_lamdaFn/assets/158173648/626469a4-807a-4044-8835-40f76878ab53)

### Similarly
![28](https://github.com/surajakdev/aws_costOptimization_lamdaFn/assets/158173648/60cc9ef0-26d9-4c66-a6d5-6ac7c71269d7)

### Run the lambda function. Here the snapshot is removed which is not attached to an instance.
![32](https://github.com/surajakdev/aws_costOptimization_lamdaFn/assets/158173648/9ea25f1d-d3d1-4ba0-92c9-87788b5fec96)









