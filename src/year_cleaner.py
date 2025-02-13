import pandas as pd
import numpy as np

class YearCleaner:
    """
    Clase para limpiar la columna 'year' del DataFrame.
    """

    def __init__(self, df):
        """
        Inicializa la clase con un DataFrame.
        
        :param df: DataFrame de Pandas con los datos originales.
        """
        self.original_df = df.copy()  # Guardamos copia del DataFrame original
        self.cleaned_df = None

    def clean_year_column(self):
        """
        Limpia la columna 'year':
        - Convierte valores a enteros de 4 dígitos
        - Elimina puntos finales
        - Rellena valores nulos o extraños con la media
        """
        if "year" in self.original_df.columns:
            self.cleaned_df = self.original_df.copy()

            # Convertir valores a enteros de 4 dígitos y eliminar puntos finales
            def clean_value(value):
                try:
                    year = int(value)
                    if year < 1000 or year > 9999:
                        return np.nan  # Consideramos valores fuera del rango como NaN
                    return year
                except (ValueError, TypeError):
                    return np.nan  # Convertimos valores problemáticos a NaN

            self.cleaned_df["year"] = self.cleaned_df["year"].apply(clean_value)

            # Rellenar valores nulos con la media
            mean_value = int(self.cleaned_df["year"].mean())
            self.cleaned_df["year"].fillna(mean_value, inplace=True)

            print("✅ Columna 'year' limpiada y valores nulos rellenados con la media.")
        else:
            print("❌ La columna 'year' no existe en el DataFrame.")

    def get_cleaned_data(self):
        """
        Devuelve el DataFrame con la columna 'year' limpia.
        
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
        "year": [2025, 2022, 2021, 2020, 2019, 2018, 2017, np.nan, 2016, 5, 0]
    })

    cleaner = YearCleaner(sample_data)
    print("🔹 Antes de la limpieza:", sample_data["year"].unique())
    cleaner.clean_year_column()
    print("🔹 Después de la limpieza:", cleaner.get_cleaned_data()["year"].unique())