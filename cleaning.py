import pandas as pd

class DataProcessor:
    """Clase para cargar, limpiar y visualizar datos."""

    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        """Carga datos desde un archivo Excel."""
        try:
            self.df = pd.read_excel(self.file_path, engine="xlrd")
            print(f"✅ Fichero {self.file_path} cargados correctamente.")
        except Exception as e:
            print(f"❌ Error al cargar el archivo {self.file_path}: {e}")

    def clean_columns(self):
        """Normaliza los nombres de las columnas."""
        if self.df is not None:
            self.df.columns = self.df.columns.str.lower().str.replace(' ', '_')
            print("✅ Columnas limpiadas.")

    def show_head(self, n=5):
        """Muestra las primeras n filas del DataFrame."""
        if self.df is not None:
            return self.df.head(n)
        else:
            print("❌ No hay datos cargados.")

    # Crea nuevo método para listar las columnas categóricas
    def categorical_columns(self):
        """Devuelve las columnas categóricas del DataFrame."""
        if self.df is not None:
            return self.df.select_dtypes(include=["object"]).columns
        else:
            print("❌ No hay datos cargados.")
    
    # Crea nuevo método para listar las columnas numéricas
    def numerical_columns(self):
        """Devuelve las columnas numéricas del DataFrame."""
        if self.df is not None:
            return self.df.select_dtypes(include=["number"]).columns
        else:
            print("❌ No hay datos cargados.")

    # Crea fn para iterar por columnas categorícas y mostrar sus valores únicos
    def unique_values(self):
        """Muestra los valores únicos de las columnas categóricas."""
        if self.df is not None:
            for col in self.categorical_columns():
                print(f"Columna: {col}")
                print(self.df[col].unique())
                print("-" * 50)
        else:
            print("❌ No hay datos cargados.")

    # Create function to retun the dataframe
    def get_data(self):
        """Devuelve el DataFrame."""
        return self.df

    # Limpia la columna 'type' que contiene estos errores: 
    # """Columna: type ['Unprovoked' 'Provoked' ' Provoked' 'Questionable' 'Watercraft' 'Sea Disaster' nan '?' 'Unconfirmed' 'Unverified' 'Invalid''Under investigation' 'Boat']""""
    def clean_type_column(self):
        """Limpia la columna 'type'."""
        if self.df is not None:
            self.df['type'] = self.df['type'].str.strip()
            print("✅ Columna 'type' limpiada.")
        else:
            print("❌ No hay datos cargados.")

    # Día 2

    # 1. GESTIÓN DE VALORES NULOS

    # - Detectar % nulos
    # - Decidir si imputamos o eliminamos
    # - Imputar con: 
    #   - númerica: media (distribución no simétrica) o mediana (simétrica)
    #   - categórica: moda (la más frecuente)

    # Crea nuevo método para detectar las columnas con valores nulos usando df.isna().sum().any()
    # Y cuenta el númeroi de nulos para cada columna con df.isna().sum()
    # Hazlo mostrando % de nulos por columna: df.isna().mean() * 100
    def missing_values(self):
        """Muestra las columnas con valores nulos y su porcentaje."""
        if self.df is not None:
            if self.df.isna().sum().any():
                print("Columnas con valores nulos:")
                print(self.df.isna().mean() * 100)
            else:
                print("✅ No hay valores nulos.")
        else:
            print("❌ No hay datos cargados.")
 
    # Crea nueva función para calcular el número de registros con muchos nulos (threshold = 3)
    def many_missing_values(self, threshold=3):
        """Calcula el número de registros con muchos valores nulos."""
        if self.df is not None:
            many_missing = self.df.isna().sum(axis=1) >= threshold
            return many_missing.sum()
        else:
            print("❌ No hay datos cargados.")

    # Crea nueva función para rellenar con un -1 los valores nulos de la columna 'X'
    def fill_nulls(self, column):
        """Rellena los valores nulos de una columna con -1."""
        if self.df is not None:
            self.df[column].fillna(-1, inplace=True)
            print(f"✅ Columna '{column}' rellenada con -1.")
        else:
            print("❌ No hay datos cargados.")

    # 2. GESTIÓN DE VALORES DUPLICADOS

    # Poner df.shape para ver la evolución del limpiado de datos

    # Crea método para detectar duplicados a través de un campo determinado (subset)
    def find_duplicates(self, subset):
        """Detecta registros duplicados."""
        if self.df is not None:
            duplicates = self.df.duplicated(subset=subset, keep=False)
            return self.df[duplicates]
        else:
            print("❌ No hay datos cargados.")

    # 3. FORMATEO DE DATOS

def main():
    print("📌 Módulo 'cleaning.py' listo para usarse.")