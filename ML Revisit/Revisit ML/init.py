import numpy as np
import pandas as pd 
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap
import seaborn as sns 
import scipy

import sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score

plt.style.use('ggplot')
sns.set_context('talk')
sns.color_palette("hls", 8)

from pprint import pprint