import objects
from load_predictions import ReadPredictions
import load_config

config = load_config.ReadConfig()
predictions = sorted(ReadPredictions(active_year = config.current_year), key = lambda Prediction: Prediction.predictor)
#sorted(student_objects, key=lambda student: student.age)
for prediction in predictions:
    print(prediction)
