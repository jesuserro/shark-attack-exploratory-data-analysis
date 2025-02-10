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

def main():
    print("📌 Módulo 'cleaning.py' listo para usarse.")