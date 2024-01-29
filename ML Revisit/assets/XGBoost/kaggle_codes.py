import pandas as pd
import urllib.request
import zipfile
from sklearn import base, pipeline
from feature_engine import encoding,imputation
from sklearn import model_selection


def read_zip(zip_filename:str='kaggle-survey-2018.zip', member_name:str="multipleChoiceResponses.csv"):
    with zipfile.ZipFile(zip_filename) as z:
        kag = pd.read_csv(z.open(member_name))
        return kag.iloc[1:]


kaggle_zip_path = r'../assets/XGBoost/kaggle-survey-2018.zip'
kaggle_member_name = r'multipleChoiceResponses.csv'


def topn(ser:pd.Series,n:int=5,default:str='other'):
    '''
    replace all values in Series that are not amoung top n , and replace with default
    '''
    counts = ser.value_counts()
    return ser.where(ser.isin(counts.index[:n]),default)


def tweak_kag(df_:pd.DataFrame)->pd.DataFrame:
    return(
        df_.assign(
        age = df_.Q2.str.slice(start=0,stop=2).astype(dtype=int,errors='raise'),
        education = df_.Q4.replace({
            "Master’s degree": 18,
            "Bachelor’s degree":16,
            "Doctoral degree":20,
            "Some college/university study without earning a bachelor’s degree":13,
            "Professional degree":19,
            "I prefer not to answer":None,
            "No formal education past high school":12
        }),
        major =df_.Q5\
                .pipe(topn,n=3)\
                .replace({
                    "Computer science (software engineering, etc.)":'cs',
                    "Engineering (non-computer focused)":'eng',
                    "Mathematics or statistics":'stat'
                }),
        years_exp = df_.Q8.str.replace('+','',regex=False).str.split('-',expand=True).iloc[:,0].astype(float),

        compensation = df_.Q9.str.replace('+','',regex=False)\
                            .str.replace(',','',regex=False)\
                            .str.replace('500000','500',regex=False)\
                            .str.replace("I do not wish to disclose my approximate yearly compensation",'0',regex=False)\
                            .str.split('-',expand=True)\
                            .iloc[:,0]
                            .fillna(0)
                            .astype(dtype=int)
                            .mul(1_000),
        python = df_.Q16_Part_1.fillna(0).replace('Python',1),
        r =  df_.Q16_Part_2.fillna(0).replace('R',1),
        sql = df_.Q16_Part_3.fillna(0).replace('SQL',1)
    ).rename(columns=lambda col:col.replace(' ','_') ).loc[:, 'Q3,age,education,major,years_exp,compensation,python,r,sql'.split(',')]
    )


class TweakKagTransformer(base.BaseEstimator,base.TransformerMixin):
    def __init__(self,ycol=None) -> None:
        self.ycol = ycol

    def transform(self,X):
        return tweak_kag(X)
    
    def fit(self,X,y=None):
        return self


def get_rawX_y(df:pd.Series,y_col:str):
    raw = df.query('Q3.isin(["United States of America", "China", "India" ]) and Q6.isin(["Data Scientist","Software Engineer"])')
    return raw.drop(columns=[y_col]),raw[y_col]


kag_pl = pipeline.Pipeline([
    ('tweak',TweakKagTransformer()),
    ('cat',encoding.OneHotEncoder(top_categories=5,drop_last=True,variables=['Q3',"major"])),
    ("num_impute",imputation.MeanMedianImputer(imputation_method='median',variables=['education','years_exp']))
])



# raw = read_zip(zip_filename=kaggle_zip_path,member_name=kaggle_member_name)
# kag_X , kag_y = get_rawX_y(df=raw,y_col='Q6')
# kag_X_train, kag_X_test, kag_y_train, kag_y_test = model_selection.train_test_split( kag_X, kag_y, test_size=.3, random_state=42, stratify=kag_y)
# X_train = kag_pl.fit_transform(kag_X_train, kag_y_train)
# X_test  = kag_pl.transform(kag_X_test)