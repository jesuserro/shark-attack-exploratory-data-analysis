import pandas as pd

def load_data(file_path):
    df = pd.read_excel(file_path, engine="xlrd")
    return df

# Create fn to retunr the first 5 rows of the data
def show_head(df):
    return df.head()

# Create function to lowercase all columns and remove spaces with underscores
def clean_columns(df):
    df.columns = df.columns.str.lower().str.replace(' ', '_')

def main():
    print("Cleaning data...")