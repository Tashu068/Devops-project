# Video Processing Setup

This repository provides a CloudFormation template to set up a video processing pipeline on AWS. The pipeline consists of an S3 input bucket, an S3 output bucket, and a Lambda function that processes uploaded video files, extracting frames every 30 seconds and saving them to the output bucket.

## Prerequisites

Before deploying the CloudFormation template, ensure you have the following:

- An AWS account
- Sufficient permissions to create resources like S3 buckets, Lambda functions, and IAM roles
- The AWS Command Line Interface (CLI) installed and configured on your local machine

## Deployment Steps

1. Clone this repository to your local machine or download the CloudFormation template (`video-processing-stack.yaml`) from the repository.

2. Open a terminal or command prompt and navigate to the directory where the CloudFormation template is located.

3. Deploy the CloudFormation stack using the AWS CLI with the following command:

    aws cloudformation create-stack --stack-name video-processing-stack --template-body file://video-processing-stack.yaml --capabilities CAPABILITY_IAM

Replace `video-processing-stack` with the desired stack name. This command creates the stack and provisions the necessary resources.

4. Wait for the stack creation to complete. You can monitor the progress in the AWS CloudFormation console or use the following AWS CLI command:

    aws cloudformation describe-stacks --stack-name video-processing-stack --query 'Stacks[0].StackStatus'


Wait until the stack status changes to `CREATE_COMPLETE`.

## Usage

Once the CloudFormation stack is created, you can start using the video processing pipeline:

1. Upload an MP4 video file to the input bucket (`my-input-bucket`). The Lambda function will be triggered automatically.

2. The Lambda function will extract frames from the video file, capturing one frame every 30 seconds.

3. The extracted frames will be saved to the output bucket (`my-output-bucket`) in JPEG format.

4. You can access the extracted frames by navigating to the output bucket in the AWS S3 console or programmatically accessing the S3 objects.

5. If you need to make changes to the pipeline configuration, you can update the CloudFormation stack and redeploy it.

## Clean Up

To clean up the resources created by the CloudFormation stack:

1. Delete any objects stored in the input and output S3 buckets.

2. Delete the CloudFormation stack using the AWS CLI with the following command:

    aws cloudformation delete-stack --stack-name video-processing-stack


Replace `video-processing-stack` with the stack name used during deployment.

3. Wait for the stack deletion to complete. You can monitor the progress in the AWS CloudFormation console or use the following AWS CLI command:

    aws cloudformation describe-stacks --stack-name video-processing-stack --query 'Stacks[0].StackStatus'



Wait until the stack status changes to `DELETE_COMPLETE`.

## Customization

- If you want to modify the frame extraction interval or any other video processing logic, you can update the `extract_frames_handler` function in the Lambda function code.

- If you want to customize the CloudFormation template or add additional resources, you can modify the `video-processing-stack.yaml` file.

---

This setup provides a basic video processing pipeline using AWS services. You can extend it or integrate other services as per your specific requirements. For more information, refer to the AWS documentation for support.



