print("Proceso etl para abarrotes")

import pandas as pd
import os 
import re
import csv 

datos = r"C:\Users\zabu\Desktop\abarrotes\customers.xlsx"
limpios = r"C:\Users\zabu\Desktop\abarrotes\customer_limpio.csv"


df = pd.read_excel(datos)

#proceso etl para customers

def etl_customer(datos, limpios):
    try: 
        df = pd.read_excel(datos)

        #eliminamos duplicados 
        
        df = df.drop_duplicates()

        #normalizamos columnas

        df.columns = (df.columns.str.lower().str.strip())

        #validamos las columnas numericas

        df['customer_id'] = pd.to_numeric(df['customer_id'], errors='coerce')

        df['age'] = pd.to_numeric(df['age'], errors='coerce')

        #rellenamos valores faltantes 

        if df['age'].isnull().any():

           mean_age = df['age'].mean()

           df['age'] = (df['age'].fillna(mean_age).any())

        df.to_csv(limpios, index=False, encoding='utf-8')

        #debugging

        print(df.info())
        print("\nvalores nulos")
        print(df.isnull().sum())
        print(f"\ndatos procesados correctamente: {len(df)}")

        return True
    
    except Exception as e:
        print(f"hubo un error en el proceso etl: {e}")
        return False
    
if __name__ == '__main__':
    etl_customer(datos, limpios)

#############################

