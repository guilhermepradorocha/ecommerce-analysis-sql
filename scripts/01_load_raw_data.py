#%%
import pandas as pd
import os 
from sqlalchemy import create_engine

data_path = 'C:/Users/User/Desktop/projects/ecommerce-analysis-sql/data'
engine = create_engine(f'sqlite:///ecommerce.db')
file_list = os.listdir(data_path)

for file_name in file_list:
    if file_name.endswith('.csv'):
        full_pathway = os.path.join(data_path, file_name)
        df = pd.read_csv(full_pathway)
        table_name = file_name.replace('olist_','').replace('_dataset.csv','')
        
        df.to_sql(
            table_name, 
            engine, 
            if_exists='replace',
            index=False
        )
print("Finished!")




# %%
