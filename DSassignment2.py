import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import RobustScaler
from sklearn.pipeline import Pipeline
df = pd.read_csv("healthcare-dataset-stroke-data.ipynb")
df_new = pd.get_dummies(df, columns=['gender','smoking_status'], drop_first=True)
df_new = df_new.drop(['id','ever_married','work_type','Residence_type'], axis=1)
df_new.hist(bins=50, figsize=(20,15))
plt.show()
