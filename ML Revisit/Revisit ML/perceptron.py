from init import *

class Perceptron:
    '''
        Perceptron Classifier (binary classifier)
        we can extend to multi-class by **one vs all* strategy

        lr: float  = learning_rate (between 0. and 1.)
        n_iter:int  = passes over the training dataset
        random_state:int = generator seed for random weights

        w_: 1d-array  = weights after fitting
        b_: scaler    = bias after fitting
        error_:list   = number of misclassification in each epoch
    '''
    def __init__(self, lr:float=0.01, n_iter:int=50, random_seed:int=1) -> None:
        self._lr:float = lr
        self._n_iter:int = n_iter
        self._random_state  = random_seed

    @property
    def lr(self)->float:
        return self._lr
    
    @property
    def n_iter(self)->int:
        return self._n_iter
    
    @property
    def random_state(self)->float:
        return self._random_state

    @lr.setter
    def lr(self,new_lr:float):
        if (isinstance(new_lr,float) and 0<new_lr<1):
            self._lr = new_lr
        else:
            raise ValueError('lr not valid')
               
    @n_iter.setter
    def n_iter(self,new_iter:int):
        self._n_iter = new_iter
    
    @random_state.setter
    def random_state(self,new_random_state:int):
        self._random_state = new_random_state


    def net_iput(self,X:np.ndarray)->np.ndarray:
        '''calc matrix multiplication'''
        return np.dot(X,self.w_)+self.b_
    
    def predict(self,X:np.ndarray)->np.ndarray:
        '''Return class label after unit step'''
        return np.where(self.net_iput(X)>=0.0,1.,0)

    def fit(self,X:np.ndarray,y:np.ndarray)->'Perceptron':
        '''
            After weights been init, the fit method loops over all individual examples in the training dataset

            $W_{i}^{T}* X_{i}+b_$
        '''
        rgen  = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0,scale=0.01,size=X.shape[1])
        self.b_ = np.float_(0.)
        self.errors_ = []

        for _ in range(self.n_iter):
            errors = 0 
            for xi, target in zip(X,y):
                update = self.lr *  (target-self.predict(xi))
                self.w_ += update*xi 
                self.b_ += update
                errors  += int(update!=0.0)
            self.errors_.append(errors)
        return self

def plot_decision_regions(X:np.ndarray,y:np.ndarray,classifer:Perceptron,resolution:float=0.02):
    '''
        helper functions to plot decision regions
    '''
    # marker
    markers = ('o','s','^','v','<')
    colors  = ('red','blue',"lightgreen",'gray','cyan')
    cmap    = ListedColormap(colors[:len(np.unique(y))])

    # plot the surface decision
    x1_min, x1_max = X[:,0].min()-1 , X[:,0].max()+1 
    x2_min, x2_max = X[:,1].min()-1 , X[:,1].max()+1 

    xx1,xx2 = np.meshgrid(
        np.arange(x1_min,x1_max,resolution),
        np.arange(x2_min,x2_max,resolution)
    )
    lab:np.ndarray = classifer.predict(
        np.array([xx1.ravel(), xx2.ravel()]).T
    )
    lab = lab.reshape(xx1.shape)
    plt.contourf(xx1,xx2,lab,alpha=0.3,cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    for idx,cl in enumerate(np.unique(y)):
        plt.scatter(
            x = X[y==cl,0],
            y = X[y==cl,1],
            alpha=0.8,
            c = colors[idx],
            marker=markers[idx],
            label=f"class {cl}",
            edgecolors='black'
        )