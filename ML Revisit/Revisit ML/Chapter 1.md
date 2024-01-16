### Giving Computers the Ability to Learn from Data

- The three different types of ML
- basic terminology and notations
- A roadmap blocks for building ML
- Installation


##### Three Different types of ML
- supervised
- unsupervised
- reinforcement

![Three Different Types of Learning](../assets/ML/different%20types%20of%20learning.png)
    


###### Supervised
    Learn a model from labeled training data that allows us to make predictions about unseen data.

- [X] Regression
    
    Prediction of continuous or ordered outcomes , called regression. 

- [X] Classification

    Predict the categorical class label (Discrete & un-ordered) of new instance based on past observation. Bi-labeled or Multi-labeled.

![Supervised Learning Process](../assets/ML/supervised%20learning%20process.png)


###### UnSupervised
    Discover hidden structure from unlabeled data. we are able to explore the structure of our data to extract meaningful information without guidance of outcome.

- [X] Clustering

    Each cluster that arises during analysis defines a group of objects that share a certain degree of similarity but are more dissimilar to objects in other clusters.

![Clustering](../assets/ML/Unsupervised%20Learning.png)

- [X] Dimensionality reduction

    Compress the data onto a smaller dimensional subspace while retaining most of the relevant information

    - PCA
    - SVD
    - T-SNE
    - Encoder



###### Reinforcement


##### Blocks for Building ML
![ML Blocks](../assets/ML/ML%20Blocks.png)


##### Installation
```sh
pip install package_name
pip install package_name --upgrade
```