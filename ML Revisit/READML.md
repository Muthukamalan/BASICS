# ML with Pytorch and Scikit-Learn

## Chapters 1: Giving Computer the Ability to Learn from Data
- [ ] Building intelligent machines to transform data into knowledge
- [ ] Three different types of machine learning
    -  making prediction about the future with supervised learning
        - Classification for predicting class labes
        -   Regression for predicting continnous outcomes
    -   solving interactive problems with RL
    -   Discovering hidden structures with unsupervised learning
        -   Finding subgreoup with clustering
        -   Dimensionality reduction for data compression

- [ ] Intro to Basic terminology and notations
- [ ] Roadmap for builidng ML systems
    -   Preprocessing getting data into shape
    -   Training and selecting a predictive model
    -   Evaluating models and predicting unseen data instances
- [ ] using python for ML
- [ ] summary

## Chapter II:  Traininf Simple ML Algo for classification
- [ ] Artifical neurons - glipse
    -   perceptron learning rule
- [ ] Implementing a perceptron learning algo in py
    -   object-oriented perceptron API
    -   Training a perceptron model on the Iris dataset
- [ ] Adaptive linear neurons and the convegence of learning
    -   Minimizing loss functions with gradient descent
    -   Implementing Adaline in python
    -   Improving gradient descent through feature scaling
    -   Large-scale ML and stochastic gradient descent

## Chapter III: Tour of ML Classifiers using scikit-Learn
- [ ] Choosing a classification algo
- [ ] First step with scikit-learn training perceptron
- [ ] Modeling class probabilities via logistic regression
- [ ] Maxmium margin classifiation with SVM
- [ ] solving nonlinear problems using a kernel SVM
- [ ] Decision tree learning
- [ ] K-nearest neighbours -a lazy learning algorithms
- [ ] summary

## Chapter IV: Building Good Training Datasets- Data preprocessing
- [ ] Dealing with missing data
- [ ] Handling categorical data
- [ ] Partioning a dataset into seperate training and test datasets
- [ ] Bringning features onto the same table
- [ ] Selecting meaningful features
- [ ] Assessing feature importance features
- [ ] Summary

## Chapter V: Compressing Data via Dimensionality Reduction
- [ ] unsupervised dimensionlity reduction via PCA
- [ ] Supervised data compression via LDA
- [ ] Nonlinear dimensionality reduction and visualization
- [ ] Summary

## Chapter VI: Learning Best Practices for Model Evaluation and Hyperparameter Tuning
- [ ] Streamlining workflows with pipelines
- [ ] Using k-fold CV to asses model performance
- [ ] Debugging algorithms with learning and validation curves
- [ ] Fine-tuning ML models via grid search
- [ ] Looking at different performance evalution metrics
- [ ] Summary

## Chapter VII: Combining Different Models for Ensemble Learning
- [ ] Learning with ensembles
- [ ] Combining classifiers via majority vote
- [ ] Bagging - building an ensemble of classifiers from bootsrap samples
- [ ] Learaging weak learners via adaptive boosting
- [ ] Gradient Boosting - training an ensemble based on loss gradients
- [ ] summary


## Chapter VIII: Applying ML to Sentiment Analysis
- [ ] Preparing the IMDb movie review data for text processing
- [ ] Intro to bag-of-words (BOW) model
- [ ] Training a logistic regression modelfor document classification
- [ ] Working with bigger data - online algorithms and out-of-core learning
- [ ] Topic modeling with latent Dirichlet allocation
- [ ] Summary

## Chapter IX: Predicting Continous Target Variables with Regression Analysis
- [ ] Intro linear regression
- [ ] Exploring the Ames Housing dataset
- [ ] Implementing on Ordinary least squares linear regression model
- [ ] Fitting a robust regression model using RANSAC
- [ ] Evaluating the performance of linear regression models
- [ ] Using regularized methods for regression
- [ ] Turing a linear regression model into a curve - polynomial regression
- [ ] Dealing with nonlinear relationships using random forests
- [ ] Summary

## Chapter X: Working with Unlabeled Data - Clustering Analysis
- [ ] Grouping objects by similarity using k-means
- [ ] organizingclusters as a hierarchical tree
- [ ] Locating regions of high density via DBSCAN
- [ ] Summary

## Chapter XI: Implementing a Multilayer ANN from scratch
- [ ] Modeling Complex functions with ANN
- [ ] Classifying handwritten idgits
- [ ] Training an ANN
- [ ] About Convergence in NN
- [ ] A few last words about NN implementation
- [ ] Summary

## Chapter XII: Parallelizing Neural Network training with Pytorch
- [ ] PyTorch and training performance
- [ ] First step with PyTorch
- [ ] Building input pipelines in PyTorch
- [ ] Building NN model in PyTorch
- [ ] Choosing activation function for multilayer NN
- [ ] Summary

## Chapter XIII: Mechanics of Pytorch
- [ ] Key features of PyTorch
- [ ] PyTorch's computation graph
- [ ] PyTorch tensor objects for storing and updating model parameters
- [ ] COmputing gradients via automatic differentiation
- [ ] Simiplifying implementaions of common architectures via torch.nn module
- [ ] **Project one** - predicting the fuel efficiency of a car
- [ ] **Project two** - classifying MNIST handwritten digits
- [ ] Higher-level PyTorch APIs: PyTorch-Lightning
- [ ] Summary

## Chapter XIV: Classifying Images with Deep CNN
- [ ] The building blocks of CNNs
- [ ] Putting everything together - implementing a CNN
- [ ] Implementing a deep CNN using PyTorch
- [ ] Implementating a deep CNN using PyTorch
- [ ] Smile Classification from face images using a CNN
- [ ] Summary

## Chapter XV: MOdeling with Sequential Data Using RNN
- [ ] Intro to sequential data
- [ ] RNNs for modeling sequences
- [ ] Implementing RNNs for sequence modeling in PyTorch
    -   **Project one** 
    -   **Project two**
- [ ] Summary

## Chapter XVI: Transformers - Improving NLP with Attention Mechanisms
- [ ] Adding an attention mechanism to RNNs
- [ ] Introducing the self attention mechanism
- [ ] Attention is all we need
- [ ] Building large-scale language models by leaveraging unlabeled data
- [ ] Fine-tuning a BERT model in PyTorch
- [ ] Summary

## Chapter XVII: Generative Adversarial networkd for Synthesizing New Data
- [ ] Introducing GAN
- [ ] Implementing a GAN from scratch
- [ ] Improving the quality of synthesized images using a convolutional and Wasserstein GAN
- [ ] Other GAN Application
- [ ] Summary

## Chapter XVIII: Graph NN for capturing Dependencies in Graph Structured Data
- [ ] Intro to graph data
- [ ] Understanding graph convolutions
- [ ] Implementing a GNN in PyTorch from scratch
- [ ] Implementing GNN using the PyTorch Geometric library
- [ ] Other GNN layers and recent developments
- [ ] Summary

## Chapter XIX: RL for Decision Making in Complex Env
- [ ] Intro learning from experience
- [ ] the Theoretical foundations of RL
- [ ] RL algo
- [ ] RL with Monto Carlo
- [ ] Implementing our first RL algo
- [ ] A galnce at deep Q-learning
- [ ] Summary

checkout: ![ML Revisit](https://sebastianraschka.com/blog/2021/ml-course.html)