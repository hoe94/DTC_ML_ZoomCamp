import bentoml
import bentoml.sklearn
from bentoml.io import NumpyNdarray
import sklearn

#First Model
#model_ref = bentoml.sklearn.get("mlzoomcamp_homework:qtzdz3slg6mwwdu5")

#Second Model
model_ref = bentoml.sklearn.get("mlzoomcamp_homework:jsi67fslz6txydu5")

model_runner = model_ref.to_runner()

svc = bentoml.Service("mlzoomcamp_model", runners = [model_runner])

@svc.api(input = NumpyNdarray(), output = NumpyNdarray())
def main(vector):
    
    prediction = model_runner.predict.run(vector)
    print(prediction)
    
    result = prediction[0]
    
    return result
