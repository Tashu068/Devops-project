import boto3
AWS_REGION = "ap-east-1"
client = boto3.client('cloudwatch', region_name=AWS_REGION)
# Create alarm
cloudwatch.put_metric_alarm(
    AlarmName='CPU-Usage',
    ComparisonOperator='GreaterThanThreshold',
    EvaluationPeriods=2,
    MetricName='CPU Utilization',
    Namespace='AWS/EC2',
    Period=2000,
    Statistic='Average',
    Threshold=80,
    ActionsEnabled=False,
    AlarmDescription='Alarm when CPU exceeds 80%',
    Dimensions=[
         {
            'Name': 'InstanceID',
            'Value': 'i-02bef29117dae8a67'
         }
    ]
)