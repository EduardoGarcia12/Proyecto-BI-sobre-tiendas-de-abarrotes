print("hola mundo")
print("proceso etl para dim_date")

import pandas as pd
import os 
import re
from datetime import datetime

datos = r"C:\Users\zabu\Desktop\abarrotes\dim_date.xlsx"
limpios = r"C:\Users\zabu\Desktop\abarrotes\dim_date_limpio.csv"

df = pd.read_excel(datos)
print(df.info())

def etl_dim_date(datos, limpios):
    try: 
        df = pd.read_excel(datos)

        #validamos las fechas 

        df['date'] = pd.to_datetime(df['date'], utc=True)

        #validamos las columnas numericas 

        df['week_number'] = pd.to_numeric(df['week_number'], errors='coerce')
        df['quarter'] = pd.to_numeric(df['quarter'], errors='coerce')
        df['day'] = pd.to_numeric(df['day'], errors='coerce')

        #rellenamos los valores faltantes

        if df['week_number'].isnull().any():
            mean_wn = df['week_number'].mean()
            df['week_number'] = (df['week_number'].fillna(mean_wn).any())

        if df['day'].isnull().any():
            mean_day = df['day'].mean()
            df['day'] = (df['day'].fillna(mean_day).any())

        if df['quarter'].isnull().any():
            mean_quarter = df['quarter'].mean()
            df['mean_quarter'] = (df['mean_quarter'].fillna(mean_day).any())

        #guardamos el csv

        df.to_csv(limpios, index=False, encoding='utf-8')

        #debugging

        print(df.info())
        print("\nvalores nulos")
        print(df.isnull().sum())
        print(f"\nlos datos procesados fueron: {len(df)}")

        return True
    
    except Exception as e: 
        print(f"el proceso etl ha fallado en: {e}")
        return False
    
if __name__ == '__main__':
    etl_dim_date(datos, limpios)