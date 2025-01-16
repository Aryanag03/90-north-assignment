# AWS Lambda: Upload File to S3

This AWS Lambda function uploads a document or PDF file to an S3 bucket. Follow the steps below to set up and deploy the function.

---

## Steps

1. **Create an S3 Bucket**:
   - Go to the [S3 Console](https://console.aws.amazon.com/s3/).
   - Click **Create bucket** and follow the instructions to create a bucket.

2. **Set Up IAM Role**:
   - Go to the [IAM Console](https://console.aws.amazon.com/iam/).
   - Create a new role with **Lambda** as the trusted entity type.
   - Attach the `AmazonS3FullAccess` policy to the role.
   - Name the role (e.g., `LambdaS3Role`).

3. **Create the Lambda Function**:
   - Go to the [AWS Lambda Console](https://console.aws.amazon.com/lambda/).
   - Click **Create function** and choose **Author from scratch**.
   - Provide a name (e.g., `UploadFileToS3`).
   - Select the runtime (`Python 3.x`) and assign the IAM role created earlier.

4. **Add Environment Variable**:
   - Under the function's **Configuration** tab, add an environment variable:
     - Key: `S3_BUCKET_NAME`
     - Value: Your S3 bucket name.

5. **Write the Code**:
   - Paste the provided Python code into the **Code** editor in the Lambda function.
   - Click **Deploy** to save changes.

6. **Test the Function**:
   - Create a test event with the following JSON format:
     ```json
     {
       "file_content": "BASE64_ENCODED_CONTENT",
       "file_name": "example.pdf"
     }
     ```
   - Replace `BASE64_ENCODED_CONTENT` with the base64-encoded file content.
   - Click **Test** to verify the upload.

7. **Verify in S3**:
   - Go to the S3 Console and check the bucket for the uploaded file.

8. **Cleanup (Optional)**:
   - Delete the Lambda function and S3 bucket if they are no longer needed.

---

## Notes

- Ensure the file content is base64-encoded before sending it to the Lambda function.
- Use `AmazonS3FullAccess` for simplicity during testing but consider applying more restrictive permissions in production.
