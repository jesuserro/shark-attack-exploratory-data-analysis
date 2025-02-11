import pandas as pd

class DataLoader:
    """
    Clase para cargar datos desde un archivo Excel y almacenarlos en un DataFrame de Pandas.
    """

    def __init__(self, file_path):
        """
        Inicializa la clase con la ruta del archivo de datos.
        
        :param file_path: Ruta del archivo de datos (Excel).
        """
        self.file_path = file_path
        self.df = None

    def load_data(self):
        """
        Carga los datos desde el archivo Excel en un DataFrame de Pandas.
        Maneja errores en caso de que el archivo no se pueda leer.
        """
        try:
            self.df = pd.read_excel(self.file_path, engine="xlrd")
            print(f"✅ Datos cargados correctamente desde {self.file_path}")
        except FileNotFoundError:
            print(f"❌ Error: No se encontró el archivo en {self.file_path}")
        except Exception as e:
            print(f"❌ Error al cargar el archivo {self.file_path}: {e}")

    def get_data(self):
        """
        Devuelve el DataFrame con los datos cargados.
        
        :return: Pandas DataFrame con los datos.
        """
        if self.df is not None:
            return self.df
        else:
            print("❌ No hay datos cargados. Usa load_data() primero.")
            return None

    def show_head(self, n=5):
        """
        Muestra las primeras n filas del DataFrame.
        
        :param n: Número de filas a mostrar (por defecto 5).
        """
        if self.df is not None:
            print(self.df.head(n))
        else:
            print("❌ No hay datos cargados. Usa load_data() primero.")

# Ejemplo de uso
if __name__ == "__main__":
    loader = DataLoader("../data/raw/GSAF5.xls")
    loader.load_data()
    loader.show_head()
