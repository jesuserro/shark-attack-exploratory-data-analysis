import pandas as pd

class ColumnCleaner:
    """
    Clase para limpiar los nombres de las columnas de un DataFrame.
    """

    def __init__(self, df):
        """
        Inicializa la clase con un DataFrame.
        
        :param df: DataFrame de Pandas con los datos originales.
        """
        self.original_df = df.copy()  # Guardamos copia del DataFrame original
        self.cleaned_df = None

    def clean_columns(self):
        """
        Limpia los nombres de las columnas:
        - Elimina espacios en blanco al inicio y final
        - Convierte a minúsculas
        - Reemplaza espacios por guiones bajos
        """
        if self.original_df is not None:
            self.cleaned_df = self.original_df.copy()
            self.cleaned_df.columns = (
                self.cleaned_df.columns
                .str.strip()
                .str.lower()
                .str.replace(' ', '_', regex=True)
            )
            print("✅ Nombres de columnas limpiados.")
        else:
            print("❌ No hay datos cargados.")

    def get_cleaned_data(self):
        """
        Devuelve el DataFrame con los nombres de columnas limpios.
        
        :return: DataFrame limpio.
        """
        return self.cleaned_df

    def save_cleaned_data(self, output_path):
        """
        Guarda el DataFrame procesado en un archivo Excel.
        
        :param output_path: Ruta donde guardar el archivo Excel.
        """
        if self.cleaned_df is not None:
            self.cleaned_df.to_excel(output_path, index=False, engine="openpyxl")
            print(f"✅ Datos limpios guardados en {output_path}")
        else:
            print("❌ No hay datos limpios para guardar.")

# Ejemplo de uso
if __name__ == "__main__":
    sample_data = pd.DataFrame({
        " Column 1 ": [1, 2, 3],
        "COLUMN 2": ["A", "B", "C"],
        "Columna_ 3": [True, False, True]
    })

    cleaner = ColumnCleaner(sample_data)
    cleaner.clean_columns()
    print(cleaner.get_cleaned_data())
