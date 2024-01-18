import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures


# TODO: Drop Duplicates and Clean Dataset
# remove duplicate records and check dtypes
def tweak_jamboree(df_:pd.DataFrame)->pd.DataFrame:
    columns = ['GRE Score', 'TOEFL Score', 'University Rating', 'SOP', 'LOR ', 'CGPA', 'Research', 'Chance of Admit ']
    return(
        df_[columns]
        .drop_duplicates()
        .astype({
            'GRE Score':'int64',
            'TOEFL Score':'int64',
            'University Rating':'int64', 
             'SOP':'float64', 
             'LOR ':'float64', 
             'CGPA':'float64', 
             'Research':'int64', 
             'Chance of Admit ':'float64'
        })
        # .pipe(debug_df)\
        .rename(columns={i:i.lower().strip().replace(' ','_') for i in df_.columns})

    )