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

def main():
    print("📌 Módulo 'cleaning.py' listo para usarse.")