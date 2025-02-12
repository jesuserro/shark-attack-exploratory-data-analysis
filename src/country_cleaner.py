import pandas as pd

class CountryCleaner:
    """
    Clase para limpiar y dar formato a la columna 'country' del DataFrame.
    """

    def __init__(self, df):
        """
        Inicializa la clase con un DataFrame y un diccionario de mapeo de países.
        
        :param df: DataFrame de Pandas con los datos originales.
        """
        self.original_df = df.copy()  # Guardamos copia del DataFrame original
        self.cleaned_df = None
        self.country_mapping = {
            'ENGLAND': 'UNITED KINGDOM',
            'NEW CALEDONIA': 'FRANCE',
            'ST HELENA, British overseas territory': 'UNITED KINGDOM',
            'REUNION': 'FRANCE',
            'FRENCH POLYNESIA': 'FRANCE',
            'Fiji': 'FIJI',
            'CAYMAN ISLANDS': 'UNITED KINGDOM',
            'ARUBA': 'NETHERLANDS',
            'ST. MARTIN': 'FRANCE',
            'DIEGO GARCIA': 'UNITED KINGDOM',
            'GUAM': 'USA',
            'TURKS & CAICOS': 'UNITED KINGDOM',
            'AZORES': 'PORTUGAL',
            'Sierra Leone': 'SIERRA LEONE',
            'ATLANTIC OCEAN': 'INTERNATIONAL WATERS',
            'GRAND CAYMAN': 'UNITED KINGDOM',
            'Seychelles': 'SEYCHELLES',
            'OKINAWA': 'JAPAN',
            'NORTHERN ARABIAN SEA': 'INTERNATIONAL WATERS',
            'CARIBBEAN SEA': 'INTERNATIONAL WATERS',
            'NORTH ATLANTIC OCEAN': 'INTERNATIONAL WATERS',
            'SOUTH CHINA SEA': 'INTERNATIONAL WATERS',
            'WESTERN SAMOA': 'SAMOA',
            'PACIFIC OCEAN ': 'INTERNATIONAL WATERS',
            'BRITISH ISLES': 'UNITED KINGDOM',
            'NEW BRITAIN': 'PAPUA NEW GUINEA',
            'JOHNSTON ISLAND': 'USA',
            'SOUTH PACIFIC OCEAN': 'INTERNATIONAL WATERS',
            'NEW GUINEA': 'PAPUA NEW GUINEA',
            'RED SEA': 'INTERNATIONAL WATERS',
            'NORTH PACIFIC OCEAN': 'INTERNATIONAL WATERS',
            'FEDERATED STATES OF MICRONESIA': 'MICRONESIA',
            'MID ATLANTIC OCEAN': 'INTERNATIONAL WATERS',
            'ADMIRALTY ISLANDS': 'PAPUA NEW GUINEA',
            'BRITISH WEST INDIES': 'INTERNATIONAL WATERS',
            'SOUTH ATLANTIC OCEAN': 'INTERNATIONAL WATERS',
            'PERSIAN GULF': 'INTERNATIONAL WATERS',
            'RED SEA / INDIAN OCEAN': 'INTERNATIONAL WATERS',
            'PACIFIC OCEAN': 'INTERNATIONAL WATERS',
            'NORTH SEA': 'INTERNATIONAL WATERS',
            'AMERICAN SAMOA': 'USA',
            'ANDAMAN / NICOBAR ISLANDAS': 'INDIA',
            'MAYOTTE': 'FRANCE',
            'NORTH ATLANTIC OCEAN ': 'INTERNATIONAL WATERS',
            'THE BALKANS': 'INTERNATIONAL WATERS',
            'SUDAN?': 'SUDAN',
            'NORTHERN MARIANA ISLANDS': 'USA',
            'IRAN / IRAQ': 'INTERNATIONAL WATERS',
            ' PHILIPPINES': 'INTERNATIONAL WATERS',
            'CENTRAL PACIFIC': 'INTERNATIONAL WATERS',
            'INDIAN OCEAN': 'INTERNATIONAL WATERS',
            'SOLOMON ISLANDS / VANUATU': 'INTERNATIONAL WATERS',
            'SOUTHWEST PACIFIC OCEAN': 'INTERNATIONAL WATERS',
            'BAY OF BENGAL': 'INDIA',
            'MID-PACIFC OCEAN': 'INTERNATIONAL WATERS',
            'CURACAO': 'NETHERLANDS',
            'ITALY / CROATIA': 'INTERNATIONAL WATERS',
            'SAN DOMINGO': 'DOMINIKANA',
            'YEMEN ': 'YEMEN',
            'REUNION ISLAND': 'FRANCE',
            'FALKLAND ISLANDS': 'UNITED KINGDOM',
            'CRETE': 'GREECE',
            'NETHERLANDS ANTILLES': 'NETHERLANDS',
            'UNITED ARAB EMIRATES (UAE)': 'UNITED ARAB EMIRATES',
            'EGYPT / ISRAEL': 'INTERNATIONAL WATERS',
            'PALESTINIAN TERRITORIES': 'INTERNATIONAL WATERS'
        }

    def clean_country_column(self):
        """
        Limpia la columna 'country':
        - Elimina espacios en blanco al inicio y final
        - Mapea los valores según el diccionario proporcionado
        """
        if "country" in self.original_df.columns:
            self.cleaned_df = self.original_df.copy()

            # Función de limpieza con apply()
            def clean_value(value):
                if pd.isna(value):
                    return None  # Convertimos NaN
                value = str(value).strip()  # Eliminamos espacios extra
                return self.country_mapping.get(value, value)  # Mapeamos el valor si está en el diccionario

            self.cleaned_df["country"] = self.cleaned_df["country"].apply(clean_value)

            print("✅ Columna 'country' limpiada.")
        else:
            print("❌ La columna 'country' no existe en el DataFrame.")

    def get_cleaned_data(self):
        """
        Devuelve el DataFrame con la columna 'country' limpia.
        
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
        "country": ["ENGLAND", "NEW CALEDONIA", "UNKNOWN", "USA"]
    })

    cleaner = CountryCleaner(sample_data)
    print("🔹 Antes de la limpieza:", sample_data["country"].unique())
    cleaner.clean_country_column()
    print("🔹 Después de la limpieza:", cleaner.get_cleaned_data()["country"].unique())