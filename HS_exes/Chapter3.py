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

advertising = pd.read_csv('Data/Advertising.csv', usecols=[1,2,3,4])
# advertising.info()

credit = pd.read_csv('Data/Credit.csv', usecols=list(range(1,12)))
credit['Student2'] = credit.Student.map({'No':0, 'Yes':1})
# print(credit.head(3))

auto = pd.read_csv('Data/Auto.csv', na_values='?').dropna()
# auto.info()

sns.regplot(advertising.TV, advertising.Sales, order=1, ci=None, scatter_kws={'color':'r'})
plt.xlim(-10,310)
plt.ylim(ymin=0)


regr = skl_lm.LinearRegression()

X = scale(advertising.TV, with_mean=True, with_std=False).reshape(-1,1)
Y = advertising.Sales

regr.fit(X,Y)
print(regr.intercept_)
print(regr.coef_)
