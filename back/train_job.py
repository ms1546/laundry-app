import sagemaker
from sagemaker import get_execution_role

role = get_execution_role()

bucket = 'your-s3-bucket-name'
data_location = f's3://{bucket}/dataset_v1/'

from sagemaker.estimator import Estimator

estimator = Estimator(
    image_uri='your-docker-image',
    role=role,
    instance_count=1,
    instance_type='ml.m5.large',
    output_path=f's3://{bucket}/output',
)

estimator.fit({'train': data_location})


#######################
# モデルのデプロイ
predictor = estimator.deploy(
    initial_instance_count=1,
    instance_type='ml.m5.large'
)
