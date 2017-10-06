# coding: utf-8
get_ipython().magic('run Chapter3.py')
get_ipython().magic('pinfo %run')
get_ipython().magic('pinfo %run')
get_ipython().magic('lsmagic')
get_ipython().magic('pinfo2 %%html')
print(_)
print(__)
print(___)
print(____)
import math
math.sin(2)
math.cos(2)
print(_)
print(__)
print(___)
print(In)
print(Out)
Out
Out[4]
Out[5]
Out[11]
Out[12]
_2
_11
math.sin(2) + math.cos(2);
Out
get_ipython().magic('history')
get_ipython().system('ls')
get_ipython().system('pwd')
get_ipython().system('echo "print from the shell"')
get_ipython().magic('cd Data/')
get_ipython().magic('ls ')
get_ipython().magic('pwd ')
get_ipython().magic('automagic')
get_ipython().magic('pinfo %automagic')
automagic1
mkdir tmp
get_ipython().magic('mkdir tmp')
ls
get_ipython().magic('ls')
get_ipython().magic('rm -r tmp')
get_ipython().magic('ls')
cd ..
get_ipython().magic('cd ..')
def func1(a, b):
    return a / b
def func2(x):
    a = x
    b = x - 1
    return func1(a, b)
func2(1)
get_ipython().magic('xmode Plain')
func2(1)
get_ipython().magic('xmode Verbose')
func2(1)
get_ipython().magic('debug')
get_ipython().magic('debug')
def func1(a, b):
    while b != 0:
        return a / b
    
func2(1)
print(func2(1))
print(func2(2))
list
h
get_ipython().magic('xmode Plain')
get_ipython().magic('pdb on')
get_ipython().magic('automagic on')
get_ipython().magic('cd Data/')
get_ipython().magic('mkdir tmp')
get_ipython().magic('ls ')
get_ipython().magic('rm -r tmp')
get_ipython().magic('ls ')
get_ipython().magic('cd ..')
get_ipython().magic('pwd ')
h
get_ipython().magic('pinfo %save')
get_ipython().magic('save -r Chapter1DSCB')
get_ipython().magic("save -r 'Chapter1DSCB'")
get_ipython().magic('save session1 1-74')
