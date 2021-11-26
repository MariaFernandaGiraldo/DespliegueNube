import pickle
import numpy as np
import json

# Load the trained model from current directory
with open('./outputs/cancer-model.pkl','rb') as model_pkl:
    lr = pickle.load(model_pkl)

if __name__ == "__main__":

 new_record = np.array([[1, 2, 3, 4, 5, 6, 8, 9]])

 predicted_result = lr.predict(new_record)

 diagnostic_clases = ['Benigno', 'Maligno']
 # return the result back
 result = json.dumps({"predicted_class": diagnostic_clases[int(predicted_result)]})

 print(result)

