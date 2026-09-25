# U01.E01 - Clasificación de Cáncer de Mama mediante SVM

## Asignatura

INF-8239 Ciencia de Datos II

## Unidad

Unidad 01 - Modelos avanzados, reducción dimensional y Green AI

## Código de la actividad

U01.E01

## Estudiante

Oscarina Brazoban Soriano

---

# Descripción del proyecto

Este proyecto desarrolla un modelo de clasificación supervisada utilizando Máquinas de Vectores de Soporte (Support Vector Machines, SVM) para predecir si un tumor es benigno o maligno a partir de características obtenidas de imágenes médicas.

El trabajo forma parte de la Unidad 01 de la asignatura Ciencia de Datos II y fue desarrollado siguiendo principios de reproducibilidad, control de versiones, validación mediante pruebas automatizadas y buenas prácticas de ingeniería de software.

---

# Pregunta de investigación

¿Es posible predecir si un tumor es benigno o maligno a partir de características extraídas de imágenes médicas utilizando un modelo de clasificación basado en Máquinas de Vectores de Soporte (SVM)?

---

# Dataset seleccionado

## Nombre

Breast Cancer Wisconsin Dataset

## Tipo de problema

Clasificación binaria supervisada

## Variable objetivo

- 0 = Maligno
- 1 = Benigno

## Características principales

- 569 observaciones
- 30 variables predictoras numéricas
- Sin valores faltantes
- Adecuado para clasificación médica

## Motivo de selección

Se seleccionó este dataset debido a que presenta una estructura limpia, ausencia de valores faltantes y una cantidad suficiente de observaciones y variables para evaluar modelos de clasificación supervisada. Además, constituye uno de los conjuntos de datos más utilizados para el estudio y evaluación de algoritmos de Machine Learning.

---

# Estructura del proyecto

```text
INFP8239_U01
│
├── data/
│
├── notebooks/
│   └── 01_svm_guiada.ipynb
│
├── reports/
│   ├── svm_best.joblib
│   └── svm_cv_results.csv
│
├── src/
│   └── inf8239_u01/
│       ├── __init__.py
│       ├── environment.py
│       └── models.py
│
├── tests/
│   ├── test_environment.py
│   └── test_models.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Requisitos

- Python 3.13 o superior
- Git
- Visual Studio Code (opcional)
- Jupyter Notebook

---

# Creación del entorno virtual

## Windows

```powershell
python -m venv .venv
```

### Activación en PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

### Activación en CMD

```cmd
.venv\Scripts\activate
```

---

# Instalación de dependencias

```bash
pip install -r requirements.txt
```

Las principales bibliotecas utilizadas son:

- numpy
- pandas
- scikit-learn
- matplotlib
- seaborn
- joblib
- pytest

---

# Ejecución del notebook

Desde la raíz del proyecto:

```bash
jupyter notebook
```

Abrir:

```text
notebooks/01_svm_guiada.ipynb
```

Ejecutar todas las celdas de principio a fin.

---

# Pruebas automatizadas

Para ejecutar todas las pruebas del proyecto:

### PowerShell

```powershell
$env:PYTHONPATH="src"
python -m pytest -q
```

### CMD

```cmd
set PYTHONPATH=src
python -m pytest -q
```

Resultado esperado:

```text
4 passed
```

---

# Metodología

El flujo de trabajo implementado incluye las siguientes etapas:

1. Carga del dataset.
2. Auditoría de calidad de datos.
3. Verificación de valores faltantes y duplicados.
4. Separación de datos en entrenamiento y prueba.
5. Construcción de una línea base mediante DummyClassifier.
6. Implementación de un Pipeline con:
   - StandardScaler
   - SVC (Support Vector Classifier)
7. Optimización de hiperparámetros mediante GridSearchCV.
8. Evaluación utilizando:
   - Accuracy
   - Precision
   - Recall
   - F1-Score
   - ROC-AUC
   - Matriz de Confusión
9. Persistencia de resultados y modelo entrenado.

---

# Prevención de fuga de información

Con el propósito de evitar problemas de Data Leakage, la división entre entrenamiento y prueba fue realizada antes de cualquier transformación de los datos.

Asimismo, la estandarización se implementó dentro de un Pipeline de Scikit-Learn utilizando StandardScaler, garantizando que los parámetros de escalado fueran calculados exclusivamente sobre el conjunto de entrenamiento.

---

# Resultados obtenidos

Se evaluaron tres configuraciones:

- Baseline mediante DummyClassifier.
- SVM con configuración base.
- SVM optimizado mediante GridSearchCV.

La búsqueda de hiperparámetros fue realizada utilizando validación cruzada estratificada de cinco particiones (Stratified K-Fold Cross Validation) y utilizando F1 Macro como criterio de selección.

Los resultados detallados se encuentran en:

```text
reports/svm_cv_results.csv
```

---

# Modelo entrenado

El mejor modelo obtenido fue almacenado mediante Joblib en:

```text
reports/svm_best.joblib
```

Esto permite reutilizar el clasificador sin necesidad de repetir el proceso de entrenamiento.

---

# Control de versiones

El proyecto utiliza Git para la gestión de versiones.

Comandos principales utilizados:

```bash
git init
git add .
git commit -m "feat: add leakage-safe SVM experiment"
```

---

# Conclusiones

Los resultados obtenidos demuestran que las Máquinas de Vectores de Soporte constituyen una alternativa efectiva para la resolución de problemas de clasificación binaria. El modelo desarrollado logró superar ampliamente el desempeño de la línea base, evidenciando una adecuada capacidad de generalización sobre datos no observados.

Asimismo, el ejercicio permitió aplicar buenas prácticas de ciencia de datos e ingeniería de software, incluyendo control de versiones, pruebas automatizadas, modularización del código, reproducibilidad y persistencia de modelos entrenados. Estas prácticas contribuyen a la construcción de soluciones más robustas, mantenibles y confiables.

---

# Autor

Oscarina Brazoban Soriano

INF-8239 Ciencia de Datos II

Maestría en Ciencia de Datos