print("hola mundo")
print("proceso etl para raw products")

import pandas as pd

datos = r"C:\Users\zabu\Desktop\abarrotes\raw_products.xlsx"
limpios = r"C:\Users\zabu\Desktop\abarrotes\raw_products_limpios.csv"


def etl_rp(datos, limpios):
    try: 
        #leemos el excel 
        df = pd.read_excel(datos)

        #validamos columnas numericas

        df['cost_price'] = pd.to_numeric(df['cost_price'], errors='coerce')
        df['sale_price'] = pd.to_numeric(df['sale_price'], errors='coerce')

        #rellenamos si es que falta algun dato 

        if df['cost_price'].isnull().any():
            mean_cp = df['cost_price'].mean()
            df['cost_price'] = (df['cost_price'].fillout(mean_cp).any())

        if df['sale_price'].isnull().any():
            mean_sp = df['sale_price'].mean()
            df['sale_price'] = (df['sale_price'].fillout(mean_sp).any())

        #guardamos el csv

        df.to_csv(limpios, index=False, encoding='utf-8')

        #debugging 
        print(df.info())
        print("\nvalores nulos: ")  
        print(df.isnull().sum())
        print(f"\nlos datos procesados fueron: {len(df)}")

        return True
    
    except Exception as e: 
        print(f"hubo un error en el proceso etl: {e}")
        return False

if __name__ == '__main__':
    etl_rp(datos, limpios)
