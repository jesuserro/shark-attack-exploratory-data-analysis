import pandas as pd

class DuplicatesCleaner:
    """
    Clase para eliminar duplicados en el DataFrame basados en la columna 'case_number'.
    """

    def __init__(self, df):
        """
        Inicializa la clase con un DataFrame.

        :param df: DataFrame de Pandas con los datos originales.
        """
        self.original_df = df.copy()  # Guardamos copia del DataFrame original
        self.cleaned_df = None

    def remove_duplicates(self):
        """
        Elimina duplicados en la columna 'case_number'.
        """
        if "case_number" in self.original_df.columns:
            self.cleaned_df = self.original_df.copy()
            
            # Mostrar tamaño antes
            print(f"\n🔹 Tamaño antes de eliminar duplicados: {self.cleaned_df.shape}")

            # Eliminar duplicados
            self.cleaned_df.drop_duplicates(subset=["case_number"], inplace=True)

            # Mostrar tamaño después
            print(f"✅ Tamaño después de eliminar duplicados: {self.cleaned_df.shape}")
        else:
            print("❌ La columna 'case_number' no existe en el DataFrame.")

    def get_cleaned_data(self):
        """
        Devuelve el DataFrame sin duplicados.

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
        "case_number": ["A001", "A002", "A003", "A002", "A004", "A001"],
        "data": [10, 20, 30, 20, 50, 10]
    })

    cleaner = DuplicatesCleaner(sample_data)
    print("🔹 Antes de la limpieza:", sample_data.shape)
    cleaner.remove_duplicates()
    print("🔹 Después de la limpieza:", cleaner.get_cleaned_data().shape)
