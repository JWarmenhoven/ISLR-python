import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import seaborn as sns

from sklearn.preprocessing import scale
import sklearn.linear_model as skl_lm
from sklearn.metrics import mean_squared_error, r2_score
import statsmodels.api as sm
import statsmodels.formula.api as smf


pd.set_option('display.notebook_repr_html', False)

plt.style.use('seaborn-white')

# advertising = pd.read_csv('Data/Advertising.csv', usecols=[1,2,3,4])
# advertising.info()

credit = pd.read_csv('Data/Credit.csv', usecols=list(range(1,12)))
credit['Student2'] = credit.Student.map({'No':0, 'Yes':1})
heads = credit.head(3)
heads

