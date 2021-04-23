import lr_function
import seaborn as sns
import pandas as pd
import numpy as np
import math
data = sns.load_dataset("tips")
print(data)
X = data["total_bill"]
Y = data["tip"]

predict = lr_function.my_regression(X, Y)

#predictions = predict(X)
predictions = predict(X)
print(predictions)
print("MAE:", np.absolute(Y - predictions).mean())