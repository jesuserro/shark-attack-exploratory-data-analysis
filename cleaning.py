import pandas as pd

def load_data(file_path):
    df = pd.read_excel(file_path, engine="xlrd")
    return df

def main():
    print("Cleaning data...")
    
    df = load_data('data/GSAF5.xls')  # Cargamos el archivo de datos

    return df.head()