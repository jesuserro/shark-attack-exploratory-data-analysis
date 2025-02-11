import pandas as pd

class TypeCleaner:
    """
    Clase para limpiar la columna 'type' del DataFrame.
    """

    def __init__(self, df):
        """
        Inicializa la clase con un DataFrame.
        
        :param df: DataFrame de Pandas con los datos originales.
        """
        self.original_df = df.copy()  # Guardamos copia del DataFrame original
        self.cleaned_df = None

    def clean_type_column(self):
        """
        Limpia la columna 'type':
        - Elimina espacios en blanco al inicio y final
        - Convierte valores dudosos en NaN
        - Normaliza valores comunes
        """
        if "type" in self.original_df.columns:
            self.cleaned_df = self.original_df.copy()

            # Función de limpieza con apply()
            def clean_value(value):
                if pd.isna(value) or value in ["?", "Unconfirmed", "Unverified", "Invalid", "Under investigation"]:
                    return None  # Convertimos valores problemáticos a NaN
                return str(value).strip()  # Eliminamos espacios extra

            self.cleaned_df["type"] = self.cleaned_df["type"].apply(clean_value)

            print("✅ Columna 'type' limpiada.")
        else:
            print("❌ La columna 'type' no existe en el DataFrame.")

    def get_cleaned_data(self):
        """
        Devuelve el DataFrame con la columna 'type' limpia.
        
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
        "type": ["Unprovoked", " Provoked", "?", "Sea Disaster", "Invalid", "Boat"]
    })

    cleaner = TypeCleaner(sample_data)
    print("🔹 Antes de la limpieza:", sample_data["type"].unique())
    cleaner.clean_type_column()
    print("🔹 Después de la limpieza:", cleaner.get_cleaned_data()["type"].unique())
