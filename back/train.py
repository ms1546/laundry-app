# AWS SageMakerでトレーニングするためのコード
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import joblib

# 仮のデータ
data = np.array([
    [20, 50, 5, 3],
    [25, 40, 10, 2.5],
    [15, 80, 3, 4],
    [30, 30, 15, 1.5]
])
X = data[:, :-1]
y = data[:, -1]

model = RandomForestRegressor()
model.fit(X, y)

joblib.dump(model, '/opt/ml/model/model.joblib')
