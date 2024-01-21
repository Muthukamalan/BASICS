# Setup

## Install Miniconda or Anaconda
[installation](https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html)

## Create new ENV
```sh
conda create --name venv python=3.10 pip
```

## Install Dependencies
```sh
pip install -r requirement.txt
```

# BASICS

## NUMPY
- [X] [Numpy Fundamentals](https://numpy.org/doc/stable/user/absolute_beginners.html)
- [X] [Enthought Numpy Tutorial](https://www.youtube.com/watch?v=ZB7BZMhfPgk)
<img src="./Learn%20Numpy/assets/numpy%20applications.png" alt="" width="350" title="Numpy Application">
- [ ] CuPy 

## PANDAS
- [X] [PyData Pandas Tutorial](https://www.youtube.com/watch?v=iYie42M1ZyU&pp=ygUTcGFuZGFzIHB5ZGF0YSB0YWxrcw%3D%3D)
- [X] [Matt Harrison - Effective Pandas](https://www.youtube.com/watch?v=zgbUk90aQ6A&pp=ygUTcGFuZGFzIHB5ZGF0YSB0YWxrcw%3D%3D)
- Beyond PANDAS
    - [ ] Duck DB 
    - [ ] Pyarrrow Integration
    - [ ] CuDF scales out to GPUs
    - [ ] Copy-on-write (COW)
    - [ ] Polars
    - [ ] Chroma vector DB

## Linear Algebra
- [ ] PCA
- [X] SVD
- [X] Fourier Series
- [ ] Gradient Descent
- [ ] [Linear Algebra](https://numpy.org/numpy-tutorials/content/tutorial-svd.html)
- [ ] Distributions


## Visualize
- [X] EDA (Python-Gallery)[https://python-graph-gallery.com/]
- [X] EDA I (matplotlib)[https://matplotlib.org/stable/tutorials/index.html]

### Kaggler
#### Olist
- [ ] [Olist Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce?datasetId=55151&sortBy=commentCount)

#### Telangana
- [ ] [Telangana Dataset](data.telangana.gov.in)


## XGBoost
- [ ] Effective XGBoost by Matt Harrison



## SciPy

SciPy is another open-source library from Python's scientific computing stack. SciPy includes submodules for integration, optimization, and many other kinds of computations that are out of the scope of NumPy itself. We will not cover SciPy as a library here, since it can be more considered as an "add-on" library on top of NumPy.