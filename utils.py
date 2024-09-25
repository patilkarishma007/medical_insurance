import pickle
import json
import numpy as np
import pandas as pd
import config

import warnings
warnings.filterwarnings("ignore")

class MedicalInsurance():
    def __init__(self):
        pass

    def __load_method(self):
        with open(config.MODEL_FILE_NAME,'rb') as f:
            self.model=pickle.load(f)

        with open(config.COLUMN_DATA_JSON,'r') as f:
            self.column_data=json.load(f)

        self.column_names =self.model.feature_names_in_
        self.feature_count =self.model.n_features_in_    

    def get_predicated_charges(self,age,gender,bmi,children,smoker,region):

        
        self.__load_method()
        gender=self.column_data['gender'][gender]
        smoker=self.column_data['smoker'][smoker]

        region="region_"+region
        region_index=np.where(self.column_names == region)[0][0]
        test_array=np.zeros((1,self.feature_count))    # 2 dimension array
        test_array[0,0]=age
        test_array[0,1]=gender
        test_array[0,2]=bmi
        test_array[0,3]=children
        test_array[0,4]=smoker
        test_array[0,region_index]=1
        predicated_charges= self.model.predict(test_array)[0]
        print('Predicated :',predicated_charges)
    
        return predicated_charges  
    
def load_dataset():

        df=pd.read_csv(config.CSV_FILE_NAME)
        #print(df)
        return df
        

