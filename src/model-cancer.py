import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
import pickle


if __name__ == "__main__":
    df = pd.read_csv("data\cell_samples.csv")

    feature_df = df[['Clump', 'UnifSize', 'UnifShape', 'MargAdh', 'SingEpiSize', 'BlandChrom', 'NormNucl', 'Mit']]

    #Datasets: Prep
    X = feature_df.values

    #Lo mapearemos a 0 para benigno y 1 para maligno
    Y = df['Class'].replace(4,1).replace(2,0)

    #Train and test data
    x_train, x_test, y_train, y_test = train_test_split(X,Y,test_size=0.25,random_state=42)
    
    
    #Estandarizar los datos 
    scaler = StandardScaler().fit(x_train) # esta linea extrae la media y la desviacion estandar de las columnas de x_train
    x_train = scaler.transform(x_train)    # esta linea resta la media y divide por la desviacion estandar cada columna

    x_test = scaler.transform(x_test)
    
    #Entrenamiento Modelo
    #hiperparametros

    clf = RandomForestClassifier(n_estimators=700)

    clf.fit(x_train,y_train) # entrenamiento

    y_pred=clf.predict(x_test) # prediccion
   
    #Accuracy
    print(accuracy_score(y_test, y_pred)) #comparamos y_test y y_pred

  

    #Register
    with open('./outputs/cancer-model.pkl', 'wb') as model_pkl:
        pickle.dump(clf, model_pkl)
        
        
# Guardar el Modelo
# clf.save('my_model.h5')

# Recrea exactamente el mismo modelo solo desde el archivo
# red_cargada = keras.models.load_model('my_model.h5')