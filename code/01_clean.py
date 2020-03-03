
import pandas as pd 
import missingno as msno 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_val_score

def clean_data(filepath): 
  
  
    df = pd.read_csv(filepath, index_col='Id')  
     
     
     
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace(' ', '_') 
     
    
      
    garage_df = df.loc[:, df.columns.str.contains('garage')]  
   
     
    for i in garage_df: 
        df[i].fillna('None', inplace=True)  
     

    fillna_cols = ['alley', 'pool_qc', 'misc_feature', 'fence', 'fireplace_qu', 'garage_qual',
                   'bsmt_qual', 'bsmt_cond', 'bsmt_exposure', 'bsmtfin_type_1', 'bsmtfin_type_2', 'mas_vnr_type']

    for i in fillna_cols:
        df[i].fillna('None', inplace=True)

    fillna_cols_0 = ['fireplace_qu',
    'lot_frontage',
    'garage_cond',
    'bsmtfin_type_1',
    'bsmt_cond',
    'bsmt_qual',
    'mas_vnr_area',
    'bsmt_half_bath',
    'bsmt_full_bath',
    'bsmtfin_sf_2',
    'bsmt_unf_sf',
    'total_bsmt_sf',
    'bsmtfin_sf_1', 
    'electrical']

    for i in fillna_cols_0:
        df[i].fillna(0, inplace=True) 

    qual_dict = {
    'Ex': 5,
    'Gd': 4,
    'TA': 3,
    'Fa': 2,
    'Po': 1, 
    'None': 0
    } 
  
    same_dict_list = ['exter_qual', 
                      'exter_cond', 
                      'bsmt_qual', 
                      'bsmt_cond', 
                      'kitchen_qual', 
                      'heating_qc', 
                      'garage_qual', 
                      'garage_cond', 
                      'fireplace_qu']
    
    for i in same_dict_list:
        df[i] = df[i].apply(qual_dict.get)  

    fence_dict = {
    'GdPrv': 4,
    'MnPrv': 3,
    'GdWo': 2,
    'MnWw': 1
    } 
    df['fence'].replace(fence_dict, inplace = True) 
     
     
    bsmtfin_type_dict = {
    'GLQ': 6,
    'ALQ': 5, 
    'BLQ': 4,
    'Rec': 3, 
    'LwQ': 2, 
    'Unf': 1,
    'None': 0
    }
     

     
    bsmt_list = ['bsmtfin_type_2', 'bsmtfin_type_1']  
    for i in bsmt_list:
        df[i] = df[i].apply(bsmtfin_type_dict.get)  
     
  
    pool_qual_dict = {'Ex': 4, 'Gd': 3, 'TA': 2, 'Fa': 1, 'None': 0} 
    df['pool_qc'].replace(pool_qual_dict, inplace = True) 
     
     
    
    df['bsmt_exposure']
    bsmt_exposure_dict = {
    'Gd': 3,
    'Av': 2,
    'Mn': 1,
    'No': 0
    } 
    df['bsmt_exposure'].replace(bsmt_exposure_dict, inplace = True) 

    df['has_pool'] = df['pool_qc'].replace({3:1, 1:1, 2:1, 4:1, 0:0})
    
    def format_neighborhood(neighborhood):
        if neighborhood == "NPkVill" or neighborhood == "Veenker" or neighborhood == "Blueste" or neighborhood == "Greens" or neighborhood ==  "GrnHill" or neighborhood == "Landmrk":
            return "other"
        else:
            return neighborhood

    df["neighborhood"] = df["neighborhood"].apply(format_neighborhood)
    
    df = pd.get_dummies(df, columns=['neighborhood'])
    df.drop(columns='neighborhood_NAmes', inplace=True)
    neighborhood_cols = [col for col in df.columns if 'neighborhood' in col]
    
    # adding interaction columns
    df['bed_bath_ratio'] = df['bedroom_abvgr']/df['full_bath']
    df['bed_bath_ratio'].fillna(0, inplace=True)
    df['bed_bath_ratio'].replace(np.inf, 0, inplace=True)
    df['garage_qual_cars'] = df['garage_qual'] * df['garage_cars']
    df['overall_cond_bed_bath'] = df['overall_cond'] * df['bed_bath_ratio']

    return df