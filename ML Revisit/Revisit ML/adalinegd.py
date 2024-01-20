from init import *

class AdalineGD:
    '''
        Adaptive Linear Neuron Classifier (binary classifier)
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

    def activation(self,X):
        '''linear activation'''
        return X
    
    def net_iput(self,X:np.ndarray)->np.ndarray:
        '''calc matrix multiplication'''
        return np.dot(X,self.w_)+self.b_
    
    def predict(self,X:np.ndarray)->np.ndarray:
        '''Return class label after unit step'''
        return np.where(self.net_iput(X)>=0.5,1.,0)

    def fit(self,X:np.ndarray,y:np.ndarray)->'AdalineGD':
        '''
            After weights been init, the fit method loops over all individual examples in the training dataset

            $W_{i}^{T}* X_{i}+b_$
        '''
        rgen  = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0,scale=0.01,size=X.shape[1])
        self.b_ = np.float_(0.)
        self.losses_ = []

        for _ in range(self.n_iter):
            net_input = self.net_iput(X)
            output    = self.activation(net_input)
            errors    = y-output
            self.w_  += self.lr * 2.0 * X.T.dot(errors)  /X.shape[0]
            self.b_  += self.lr * 2.0 * errors.mean() 
            loss      = (errors**2 ).mean()
            self.losses_.append(loss)
            
        return self
