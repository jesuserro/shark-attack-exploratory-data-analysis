# Shark Attacks

## Estructura

```
shark_attacks_project/
│── data/                        # Carpeta para almacenar los datos
│   ├── raw/                     # Datos originales sin procesar
│   │   ├── GSAF5.xls            # Archivo Excel con los datos de ataques de tiburones
│   ├── processed/                # Datos limpios y transformados
│   ├── final/                    # Datos listos para su análisis
│
│── notebooks/                    # Notebooks de Jupyter para análisis y documentación
│   ├── main.ipynb                # Notebook principal con análisis y explicación para el cliente
│   ├── exploratory_analysis.ipynb # Análisis exploratorio inicial (EDA)
│
│── src/                          # Código fuente de las clases y funciones
│   ├── __init__.py               # Hace que esta carpeta sea un paquete Python
│   ├── data_loader.py            # Clase para cargar datos
│   ├── cleaner.py                # Clase para limpiar y normalizar los datos
│   ├── nullator.py               # Clase para gestionar valores nulos
│   ├── duplicator.py             # Clase para manejar duplicados
│   ├── filtrator.py              # Clase para filtrar columnas relevantes
│   ├── analyzer.py               # Clase para análisis inicial (EDA)
│   ├── visualizer.py             # Clase para visualización de datos
│
│── scripts/                      # Scripts ejecutables de automatización
│   ├── run_cleaning.py           # Script para ejecutar la limpieza de datos
│   ├── run_analysis.py           # Script para ejecutar el análisis final
│
│── reports/                      # Documentación y reportes generados
│   ├── figures/                  # Gráficos generados en el análisis
│   ├── summary.md                # Resumen del análisis para el cliente
│
│── tests/                        # Pruebas unitarias para el código
│   ├── test_cleaner.py           # Pruebas para la clase Cleaner
│   ├── test_nullator.py          # Pruebas para la clase Nullator
│   ├── test_duplicator.py        # Pruebas para la clase Duplicator
│
│── .gitignore                     # Archivos a ignorar en Git
│── README.md                      # Documentación del proyecto
│── requirements.txt               # Lista de paquetes de Python necesarios
│── setup.py                       # Script de instalación del paquete (opcional)

```
