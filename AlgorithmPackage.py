
# coding: utf-8

#%% 

#基础
import os
import time 
from datetime import  datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
plt.rcParams['font.sans-serif']=['SimHei']
from sklearn.pipeline import make_pipeline
import multiprocessing as mp
import csv
from sklearn.metrics import confusion_matrix

#数据处理
from sklearn.cross_validation import train_test_split
#from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
#from sklearn.cross_validation import KFold
from sklearn.model_selection import KFold
from sklearn.cross_validation import StratifiedKFold
from sklearn.cross_validation import LeaveOneOut
from sklearn.cross_validation import cross_val_score
import collections
from sklearn import datasets
import codecs


#广义线性与插值
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from scipy.interpolate import KroghInterpolator
from scipy.interpolate import lagrange
from scipy.interpolate import BarycentricInterpolator
from scipy.interpolate import PchipInterpolator
from scipy.interpolate import PPoly,interp1d,splrep,splev
#聚类与降唯

from sklearn.cluster import KMeans
from sklearn.cluster import AffinityPropagation
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import Birch
from sklearn.cluster import DBSCAN
from sklearn.cluster import FeatureAgglomeration
from sklearn.cluster import MiniBatchKMeans
from sklearn.cluster import MeanShift
from sklearn.cluster import SpectralClustering

from sklearn.manifold import TSNE
from sklearn.decomposition import PCA

##机器学习模型-无监督距离
from sklearn.neighbors import BallTree
from sklearn.neighbors import KDTree
from sklearn.neighbors import LSHForest


#机器学习模型-分类
from sklearn.externals import joblib

from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis,QuadraticDiscriminantAnalysis
from sklearn.linear_model import SGDClassifier,PassiveAggressiveClassifier,RidgeClassifier,RidgeClassifierCV
from sklearn.dummy import DummyClassifier
from sklearn.tree import DecisionTreeClassifier#,ExtraTreeClassifier
from sklearn.svm import SVC,LinearSVC,NuSVC
from sklearn.naive_bayes import GaussianNB,BernoulliNB,MultinomialNB
from sklearn.neighbors import KNeighborsClassifier,NearestNeighbors,RadiusNeighborsClassifier
from sklearn.ensemble import ExtraTreesClassifier,RandomForestClassifier,AdaBoostClassifier,GradientBoostingClassifier,BaggingClassifier
from sklearn.semi_supervised import LabelPropagation,LabelSpreading
from sklearn.ensemble import VotingClassifier,RandomTreesEmbedding

#机器学习模型-回归

from sklearn.linear_model import LinearRegression
from sklearn.dummy import DummyRegressor
from sklearn.tree import DecisionTreeRegressor,ExtraTreeRegressor
from sklearn.svm import SVR,LinearSVR,NuSVR
from sklearn.neighbors import KNeighborsRegressor,RadiusNeighborsRegressor
from sklearn.ensemble import ExtraTreesRegressor,RandomForestRegressor,AdaBoostRegressor,GradientBoostingRegressor,BaggingRegressor