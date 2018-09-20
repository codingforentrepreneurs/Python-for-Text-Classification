# Python for Text Classification
Python for Text Classification with Machine Learning in Python 3.6.


### Installation Guide

Start your environment by picking either pipenv (recommended) or virtualenv. Simple guides are below.

#### Using pipenv
1. Initialize pipenv ([setup guide](https://www.codingforentrepreneurs.com/blog/pipenv-virtual-environments-for-python/)):
```
cd path/to/your/dev/folder
mkdir text-classify
cd text-classify
pipenv install --three
```
After installation of pipenv works, just activate it (same on all systems):
```
pipenv shell
```
2. Project requirements
```
pip install numpy scipy scikit-learn jupyter
```


#### Using virtualenv
1. Initialize virtualenv
```
cd path/to/your/dev/folder
mkdir text-classify
cd text-classify
virtualenv --python3 .
```
After installation of pipenv works, just activate it:

Mac / Linux
```
source bin/activate
```

Windows

```
.\Scripts\activate
```


2. Project requirements
```
pip install numpy scipy scikit-learn jupyter
```
