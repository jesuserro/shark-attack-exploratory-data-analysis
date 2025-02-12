import pandas as pd
import re

class TimeCleaner:
    """
    Clase para limpiar y dar formato a la columna 'time' del DataFrame.
    """

    def __init__(self, df):
        """
        Inicializa la clase con un DataFrame.
        
        :param df: DataFrame de Pandas con los datos originales.
        """
        self.original_df = df.copy()  # Guardamos copia del DataFrame original
        self.cleaned_df = None

    def clean_time_column(self):
        """
        Limpia la columna 'time':
        - Convierte los valores a tres categorías: mañana ("M"), tarde ("T") y noche ("N")
        - Rellena valores nulos o no concluyentes con "Unknown"
        """
        if "time" in self.original_df.columns:
            self.cleaned_df = self.original_df.copy()

            # Función de limpieza con apply()
            def clean_value(value):
                if pd.isna(value) or value in ["Unknown", "   ", "FATAL  (Wire netting installed at local beaches after this incident.)"]:
                    return "Unknown"  # Convertimos valores problemáticos a "Unknown"
                value = str(value).strip().lower()
                if re.search(r'\b(morning|early morning|midday|before|am|dawn)\b', value):
                    return "M"  # Mañana
                elif re.search(r'\b(afternoon|evening|pm|dusk|sunset|late afternoon)\b', value):
                    return "T"  # Tarde
                elif re.search(r'\b(night|midnight|after midnight)\b', value):
                    return "N"  # Noche
                else:
                    try:
                        hour = int(re.search(r'\d{1,2}', value).group())
                        if 5 <= hour < 12:
                            return "M"  # Mañana
                        elif 12 <= hour < 18:
                            return "T"  # Tarde
                        else:
                            return "N"  # Noche
                    except:
                        return "Unknown"  # Si no se puede determinar, se marca como "Unknown"

            self.cleaned_df["time"] = self.cleaned_df["time"].apply(clean_value)

            print("✅ Columna 'time' limpiada.")
        else:
            print("❌ La columna 'time' no existe en el DataFrame.")

    def get_cleaned_data(self):
        """
        Devuelve el DataFrame con la columna 'time' limpia.
        
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
        "time": ['Unknown', '07h53', '14h00', '16h10', '07h00', None, '11h17', '12h00', '16h00', '11h30', '12h30', '15h00', '17h45', '10jh45', 'Early morning', '17h30', '13h12', '18h00', '07h30', '11hoo', '11h43', '10h15', '13h00', '20h00', 'Afternoon', '14h09', '10h40', '12h15', '19h12', 'Morning', '10h00', '15h20', '16h40', '15h30', '07h50', '12h50', '16h30', '11h15', '07h31', '14h45', '06h30', '10h30', '19h20', 'Dusk', '09h00', '13h20', '11h45', '06h40', '`17h00', '07h51', '11h46', '11h00', '13h30', '20h30', '12h23', '07h07', '16h39', '13h50', '07h15', '09h15', '15h57', '14h30', '11h20', '16h45', '08h00', '10j30', '08h15', '08h56', '15h40', '19h00', '18h30', '07h45', '17h00', '07h58', '17h40', '09h00-10h00', '17h10', '09h36', '14h20', '08h40', '06h00', 'Sunset', '10h45', 1415, '09h30', '14h00-15h00', '14h15', '09h08', 'Evening', '15h59', '08h30', '12h20', '10h50', 'Midday', 'Early Morning', '09h40', '14h33', '12h58', '"Evening"', '16h15', '06h50', '10h20', '12h45', '11h55', '19h30', '22h20', '08h48', '16h21', '16h26', '18h45', 'Night', '01h00', '03h00', '13h40', '06h15', 'Before 10h00', '06h45', 'Early afternoon', '06h55', '13h45', '13h15', '09h29', '10h47', '14h11', '15h35', '14h40', '14h00  -15h00', 'Late afternoon', '16h50', '21h50', '17h35', '19h00, Dusk', '15h01', '23h30', '10h44', '13h19', '15h45', 'Shortly before 12h00', '17h34', '08h50', '02h00', '09h50', '9h00', '10h43', 'After noon', '15h15', '19h05', 1300, '14h30 / 15h30', '22h00', '16h20', '14h34', '15h25', '14h55', '17h46', 'Morning ', '15h49', 'Midnight', '09h30 / 10h00', '18h15', '04h00', '14h50', 'FATAL  (Wire netting installed at local beaches after this incident.)', '01h30', 'After midnight', 'Late afternon', '05h30', '08h58', '"Early evening"', 'Late Afternoon', '   ', 'Before daybreak', 'dusk', 'Before 10h30', '06h00 -- 07h00', '01h50', '17h00-18h00', '19h00-20h00']
    })

    cleaner = TimeCleaner(sample_data)
    print("🔹 Antes de la limpieza:", sample_data["time"].unique())
    cleaner.clean_time_column()
    print("🔹 Después de la limpieza:", cleaner.get_cleaned_data()["time"].unique())