# ISLR-python
This repository contains Python code for a selection of tables, figures and LAB sections from the book <A target="_blank" href='http://www-bcf.usc.edu/%7Egareth/ISL/index.html'>'An Introduction to Statistical Learning with Applications in R'</A> by James, Witten, Hastie, Tibshirani (2013).<P>

**2018-01-15**:<BR>
Minor updates to the repository due to changes/deprecations in several packages. The notebooks have been tested with <A href='http://nbviewer.jupyter.org/github/JWarmenhoven/ISLR-python/blob/master/Notebooks/Python%20module%20versions.ipynb'>these package versions</A>. Thanks @lincolnfrias and @telescopeuser.
<P>

**2016-08-30**:<BR>
Chapter 6: I included Ridge/Lasso regression code using the new <A href='https://github.com/civisanalytics/python-glmnet'>python-glmnet</A> library. This is a python wrapper for the Fortran library used in the *R* package *glmnet*. 
<P>

<IMG src='http://www-bcf.usc.edu/%7Egareth/ISL/ISL%20Cover%202.jpg' height=20% width=20%> <P>
<A href='http://nbviewer.ipython.org/github/JWarmenhoven/ISL-python/blob/master/Notebooks/Chapter%203.ipynb'>Chapter 3 - Linear Regression</A><BR>
<A href='http://nbviewer.ipython.org/github/JWarmenhoven/ISL-python/blob/master/Notebooks/Chapter%204.ipynb'>Chapter 4 - Classification</A><BR>
<A href='http://nbviewer.ipython.org/github/JWarmenhoven/ISL-python/blob/master/Notebooks/Chapter%205.ipynb'>Chapter 5 - Resampling Methods</A><BR>
<A href='http://nbviewer.ipython.org/github/JWarmenhoven/ISL-python/blob/master/Notebooks/Chapter%206.ipynb'>Chapter 6 - Linear Model Selection and Regularization</A><BR>
<A href='http://nbviewer.ipython.org/github/JWarmenhoven/ISL-python/blob/master/Notebooks/Chapter%207.ipynb'>Chapter 7 - Moving Beyond Linearity</A><BR>
<A href='http://nbviewer.ipython.org/github/JWarmenhoven/ISL-python/blob/master/Notebooks/Chapter%208.ipynb'>Chapter 8 - Tree-Based Methods</A><BR>
<A href='http://nbviewer.ipython.org/github/JWarmenhoven/ISL-python/blob/master/Notebooks/Chapter%209.ipynb'>Chapter 9 - Support Vector Machines</A><BR>
<A href='http://nbviewer.ipython.org/github/JWarmenhoven/ISL-python/blob/master/Notebooks/Chapter%2010.ipynb'>Chapter 10 - Unsupervised Learning</A><P>
<A href='http://nbviewer.jupyter.org/github/JWarmenhoven/ISL-python/blob/master/Notebooks/Simulate.expected.misclassification.rate.ipynb'>Extra: Misclassification rate simulation - SVM and Logistic Regression</A><P>
This great book gives a thorough introduction to the field of Statistical/Machine Learning. The book is available for download (see link below), but I think this is one of those books that is definitely worth buying. The book contains sections with applications in R based on public datasets available for download or which are part of the <A target="_blank" href="https://cran.r-project.org/web/packages/ISLR/index.html">R-package ISLR</A>. Furthermore, there is a Stanford University online course based on this book and taught by the authors (See <A target="_blank" href='https://lagunita.stanford.edu/courses/'>course catalogue</A> for current schedule).<P>
Since Python is my language of choice for data analysis, I decided to try and do some of the calculations and plots in Jupyter Notebooks using:

 - pandas
 - numpy
 - scipy
 - scikit-learn
 - python-glmnet
 - statsmodels
 - patsy
 - matplotlib
 - seaborn

It was a good way to learn more about Machine Learning in Python by creating these notebooks. I created some of the figures/tables of the chapters and worked through some LAB sections. At certain points I realize that it may look like I tried too hard to make the output identical to the tables and R-plots in the book. But I did this to explore some details of the libraries mentioned above (mostly matplotlib and seaborn). Note that this repository is <STRONG>not a standalone tutorial</STRONG> and that you probably should have a copy of the book to follow along. Suggestions for improvement and help with unsolved issues are welcome!
See Hastie et al. (2009) for an advanced treatment of these topics.<P> 

For Bayesian data analysis, take a look at <A href='https://github.com/JWarmenhoven/DBDA-python'>this notebook</A>.

#### References: 
James, G., Witten, D., Hastie, T., Tibshirani, R. (2013). <I>An Introduction to Statistical Learning with Applications in  R</I>,  Springer Science+Business Media, New York.
http://www-bcf.usc.edu/~gareth/ISL/index.html

Hastie, T., Tibshirani, R., Friedman, J. (2009). <I>Elements of Statistical Learning</I>, Second Edition, Springer Science+Business Media, New York.
http://statweb.stanford.edu/~tibs/ElemStatLearn/
