import pandas as pd

class SexCleaner:
    """
    Clase para limpiar la columna 'sex' en el DataFrame.
    """

    def __init__(self, df):
        """
        Inicializa la clase con un DataFrame.
        
        :param df: DataFrame de Pandas con los datos originales.
        """
        self.original_df = df.copy()  # Guardamos copia del DataFrame original
        self.cleaned_df = None

    def clean_sex_column(self):
        """
        Limpia la columna 'sex':
        - Elimina espacios en blanco al inicio y final
        - Convierte valores incorrectos en NaN
        - Normaliza los valores a 'M' o 'F'
        """
        if "sex" in self.original_df.columns:
            self.cleaned_df = self.original_df.copy()

            # Función de limpieza con apply()
            def clean_value(value):
                if pd.isna(value):
                    return None  # Mantener nulos como None
                value = str(value).strip()  # Eliminar espacios extra
                
                # Normalizar valores correctos
                if value in ["M", "F"]:
                    return value
                
                # Reemplazar valores inconsistentes con None
                if value in ["M x 2", "lli", "N", "."]:
                    return None
                
                return value  # Devolver el valor si no es inconsistente

            self.cleaned_df["sex"] = self.cleaned_df["sex"].apply(clean_value)

            print("✅ Columna 'sex' limpiada.")
        else:
            print("❌ La columna 'sex' no existe en el DataFrame.")

    def get_cleaned_data(self):
        """
        Devuelve el DataFrame con la columna 'sex' limpia.
        
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
        "sex": ["F", " M", "M ", "M x 2", "N", "lli", ".", "F"]
    })

    cleaner = SexCleaner(sample_data)
    print("🔹 Antes de la limpieza:", sample_data["sex"].unique())
    cleaner.clean_sex_column()
    print("🔹 Después de la limpieza:", cleaner.get_cleaned_data()["sex"].unique())
