import boto3
from flask import Flask, jsonify
from sagemaker import Predictor
from sagemaker.serializers import JSONSerializer

app = Flask(__name__)

# SageMakerエンドポイントの設定
predictor = Predictor(endpoint_name='drying-time-endpoint', serializer=JSONSerializer())

@app.route('/start-laundry', methods=['POST'])
def start_laundry():
    temperature = 25
    humidity = 60
    wind_speed = 5

    data = {
        "instances": [[temperature, humidity, wind_speed]]
    }
    drying_hour = predictor.predict(data)['predictions'][0]

    return jsonify({'dryinghour': drying_hour})

if __name__ == '__main__':
    app.run(debug=True)
