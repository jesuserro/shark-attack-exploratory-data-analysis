import pandas as pd

class FatalCleaner:
    """
    Clase para limpiar y dar formato a la columna 'fatal_y/n' del DataFrame.
    """

    def __init__(self, df):
        """
        Inicializa la clase con un DataFrame.
        
        :param df: DataFrame de Pandas con los datos originales.
        """
        self.original_df = df.copy()  # Guardamos copia del DataFrame original
        self.cleaned_df = None

    def clean_fatal_column(self):
        """
        Limpia la columna 'fatal_y/n':
        - Renombra la columna a 'fatal'
        - Convierte los valores a booleanos (1 para fatal, 0 para no fatal)
        - Rellena valores nulos o no concluyentes con la moda
        """
        if "fatal_y/n" in self.original_df.columns:
            self.cleaned_df = self.original_df.copy()
            self.cleaned_df.rename(columns={"fatal_y/n": "fatal"}, inplace=True)

            # Función de limpieza con apply()
            def clean_value(value):
                if pd.isna(value) or value in ["UNKNOWN", "Nq", "F", 2017, " N", "N "]:
                    return None  # Convertimos valores problemáticos a NaN
                if str(value).strip().upper() in ["Y", "Y X 2"]:
                    return 1  # Fatal
                return 0  # No fatal

            self.cleaned_df["fatal"] = self.cleaned_df["fatal"].apply(clean_value)

            # Rellenar valores nulos con la moda
            mode_value = self.cleaned_df["fatal"].mode()[0]
            self.cleaned_df["fatal"] = self.cleaned_df["fatal"].fillna(mode_value)

            print("✅ Columna 'fatal' limpiada.")
        else:
            print("❌ La columna 'fatal_y/n' no existe en el DataFrame.")

    def get_cleaned_data(self):
        """
        Devuelve el DataFrame con la columna 'fatal' limpia.
        
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
        "fatal_y/n": ["N", "Y", "M", "n", None, "Nq", "F", "UNKNOWN", 2017, "Y x 2", " N", "N ", "y"]
    })

    cleaner = FatalCleaner(sample_data)
    print("🔹 Antes de la limpieza:", sample_data["fatal_y/n"].unique())
    cleaner.clean_fatal_column()
    print("🔹 Después de la limpieza:", cleaner.get_cleaned_data()["fatal"].unique())