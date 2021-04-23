from lr_function import my_regression
from data_input import save_to_csv,getData

import pandas as pd
import numpy as np

#get data
X,Y=getData()

#get rL function
predict = my_regression(X, Y)

#run predictions using rL
predictions = predict(X)

print("MAE:", np.absolute(Y - predictions).mean())

"""
for i in range(len(predictions)):
    print("X: ",X[i] ,"Y: ",Y[i] ,"pred: ", predictions[i])
"""
#save the results 
print("-----------\n\n\n")

res = np.array([X, Y,predictions])
pred_res=pd.DataFrame(res)
save_to_csv(pred_res,"predictions")
