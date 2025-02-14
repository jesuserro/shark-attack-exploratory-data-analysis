import pandas as pd

class ActivityCleaner:
    """
    Clase para limpiar la columna 'activity' del DataFrame.
    """

    def __init__(self, df):
        """
        Inicializa la clase con un DataFrame.
        
        :param df: DataFrame de Pandas con los datos originales.
        """
        self.original_df = df.copy()  # Guardamos copia del DataFrame original
        self.cleaned_df = None

    def clean_activity_column(self):
        """
        Limpia la columna 'activity':
        - Rellena nulos con la moda
        - Elimina espacios en blanco al inicio y final
        - Normaliza valores comunes
        """
        if "activity" in self.original_df.columns:
            self.cleaned_df = self.original_df.copy()

            # Función de limpieza con apply()
            def clean_value(value):
                if pd.isna(value):
                    return None  # Convertimos valores problemáticos a NaN
                return str(value).strip()  # Eliminamos espacios extra

            self.cleaned_df["activity"] = self.cleaned_df["activity"].apply(clean_value)

            # Rellenar valores nulos con la moda
            mode_value = self.cleaned_df["activity"].mode()[0]
            self.cleaned_df["activity"] = self.cleaned_df["activity"].fillna(mode_value)

            print("✅ Columna 'activity' limpiada.")
        else:
            print("❌ La columna 'activity' no existe en el DataFrame.")

    def get_cleaned_data(self):
        """
        Devuelve el DataFrame con la columna 'activity' limpia.
        
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
        "activity": ["Swimming", " Swimming", None, "Surfing", "Swimming "]
    })

    cleaner = ActivityCleaner(sample_data)
    print("🔹 Antes de la limpieza:", sample_data["activity"].unique())
    cleaner.clean_activity_column()
    print("🔹 Después de la limpieza:", cleaner.get_cleaned_data()["activity"].unique())