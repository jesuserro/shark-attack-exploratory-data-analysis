import pandas as pd

class SpeciesCleaner:
    """
    Clase para limpiar la columna 'species' del DataFrame.
    """

    def __init__(self, df):
        """
        Inicializa la clase con un DataFrame.
        
        :param df: DataFrame de Pandas con los datos originales.
        """
        self.original_df = df.copy()  # Guardamos copia del DataFrame original
        self.cleaned_df = None

    def clean_species_column(self):
        """
        Limpia la columna 'species':
        - Normaliza nombres de especies
        - Agrupa especies por tamaño
        - Rellena valores nulos y 'Unknown' con la moda
        """
        if "species" in self.original_df.columns:
            self.cleaned_df = self.original_df.copy()

            # Mapeo de especies por tamaño
            species_mapping = {
                "White shark": "Large",
                "Tiger shark": "Large",
                "Bull shark": "Large",
                "6' shark": "Medium",
                "4' shark": "Small",
                "1.8 m [6'] shark": "Medium",
                "1.5 m [5'] shark": "Small",
                "5' shark": "Small",
                "1.2 m [4'] shark": "Small",
                "4' to 5' shark": "Small",
                "2 m shark": "Medium",
                "3' shark": "Small",
                "3 m [10'] shark": "Large",
                "Nurse shark": "Medium",
                "Blacktip shark": "Medium",
                "3' to 4' shark": "Small",
                "3 m shark": "Large",
                "2.4 m [8'] shark": "Medium",
                "12' shark": "Large",
                "3.7 m [12'] shark": "Large",
                "Blue shark": "Large",
                "7' shark": "Medium",
                "1.2 m to 1.5 m [4' to 5'] shark": "Small",
                "Mako shark": "Large",
                "1.5 m shark": "Small",
                "Bronze whaler shark": "Medium",
                "Raggedtooth shark": "Medium",
                "6 m [20'] white shark": "Large",
                "10' shark": "Large",
                "5 m [16.5'] white shark": "Large",
                "Grey nurse shark": "Medium",
                "Zambesi shark": "Medium",
                "Sandtiger shark": "Medium",
                "Hammerhead shark": "Large",
                "Oceanic whitetip shark": "Large",
                "Lemon shark": "Medium",
                "4 m [13'] white shark": "Large",
                "8' shark": "Medium",
                "2' to 3' shark": "Small",
                "2.1 m [7'] shark": "Medium",
                "1 m shark": "Small",
                "Bull shark, 6'": "Medium",
                "9' shark": "Medium",
                "3 m [10'] white shark": "Large",
                "2.5 m shark": "Medium",
                "Spinner shark": "Medium",
                "1.8 m shark": "Medium",
                "Basking shark": "Large",
                "2' shark": "Small",
                "5' to 6' shark": "Medium",
                "14' shark": "Large",
                "4 m to 5 m [13' to 16.5'] white shark": "Large",
                "Angel shark": "Medium",
                "6' to 8' shark": "Medium",
                "2.5 m [8.25'] white shark": "Medium",
                "1.8 m [6'] blacktip shark": "Medium",
                "4.3 m [14'] shark": "Large",
                "3 m [10'] bull shark": "Large",
                "1.8 m to 2.4 m [6' to 8'] shark": "Medium",
                "15' shark": "Large",
                "13' shark": "Large",
                "4.6 m [15'] shark": "Large",
                "Sevengill shark": "Medium",
                "0.9 m [3'] shark": "Small",
                "5 m to 6 m [16.5' to 20'] white shark": "Large",
                "5.5 m [18'] white shark": "Large",
                "Grey reef shark": "Medium",
                "Tiger shark, 3 m [10']": "Large",
                "4 m [13'] shark": "Large",
                "Caribbean reef shark": "Medium",
                "Bull shark, 4' to 5'": "Small"
            }

            # Función de limpieza con apply()
            def clean_value(value):
                if pd.isna(value) or value in ["?", "Invalid", "No shark involvement", "Shark involvement not confirmed"]:
                    return None  # Convertimos valores problemáticos a NaN
                return species_mapping.get(value, "Unknown")  # Mapeamos especies o asignamos "Unknown"

            self.cleaned_df["species"] = self.cleaned_df["species"].apply(clean_value)

            # Rellenar valores nulos y 'Unknown' con la moda
            valid_species = self.cleaned_df["species"][self.cleaned_df["species"] != "Unknown"]
            mode_value = valid_species.mode()[0]
            self.cleaned_df["species"].fillna(mode_value, inplace=True)
            self.cleaned_df["species"].replace("Unknown", mode_value, inplace=True)

            print("✅ Columna 'species' limpiada y valores nulos y 'Unknown' rellenados con la moda.")
        else:
            print("❌ La columna 'species' no existe en el DataFrame.")

    def get_cleaned_data(self):
        """
        Devuelve el DataFrame con la columna 'species' limpia.
        
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
        "species": ["White shark", "Tiger shark", "?", "6' shark", "Invalid", "Bull shark"]
    })

    cleaner = SpeciesCleaner(sample_data)
    print("🔹 Antes de la limpieza:", sample_data["species"].unique())
    cleaner.clean_species_column()
    print("🔹 Después de la limpieza:", cleaner.get_cleaned_data()["species"].unique())