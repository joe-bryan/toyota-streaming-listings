aws \
cloudformation deploy \
--template-file s3-stack.yaml \
--stack-name S3streaming \
--capabilities CAPABILITY_IAM \