```zsh
# AWS CLIを使用してトレーニングジョブを開始
aws sagemaker create-training-job --training-job-name drying-time-predictor \
    --algorithm-specification TrainingImage=<your-docker-image> \
    --role-arn <your-sagemaker-execution-role> \
    --input-data-config ChannelName=training,DataSource={...} \
    --output-data-config S3OutputPath=<your-s3-output-path> \
    --resource-config InstanceType=ml.m5.large,InstanceCount=1,VolumeSizeInGB=10 \
    --stopping-condition MaxRuntimeInSeconds=3600
```
