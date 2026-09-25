# U01.E01 - Clasificacion de tumores con SVM

Entrega individual para INF-8239 Ciencia de Datos II.

## Pregunta

Es posible predecir si un tumor es benigno o maligno a partir de caracteristicas numericas obtenidas de imagenes medicas usando una Maquina de Vectores de Soporte?

## Dataset aprobado

Se compararon dos opciones: Iris, con 150 observaciones, 4 variables y 3 clases botanicas, y Breast Cancer Wisconsin Diagnostic, con 569 observaciones, 30 variables numericas y 2 clases diagnosticas. Se aprobo Breast Cancer Wisconsin porque responde directamente a la pregunta de investigacion y permite estudiar una clasificacion binaria con mayor volumen de datos. El dataset se carga reproduciblemente mediante `sklearn.datasets.load_breast_cancer`; su origen es UCI Machine Learning Repository y la distribucion dentro de scikit-learn se realiza bajo BSD-3-Clause.

## Estructura

```text
data/                 Datos locales, si aplica
notebooks/            Notebook ejecutado y verificacion del entorno
reports/              CSV, modelo serializado y PDF de entrega
src/inf8239_u01/      Codigo reutilizable
tests/                Pruebas automatizadas
requirements.txt      Dependencias
```

## Instalacion reproducible en Windows

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
$env:PYTHONPATH="src"
```

## Ejecucion

Ejecutar de principio a fin `notebooks/01_svm_guiada.ipynb`. El notebook carga el dataset, audita tipos, ausentes y duplicados, separa train/test con estratificacion, compara contra `DummyClassifier`, ajusta un pipeline `StandardScaler` + `SVC`, selecciona hiperparametros con `GridSearchCV` y guarda resultados.

```powershell
$env:PYTHONPATH="src"
python -m pytest -q
python reports/generate_pdf.py
```

El informe queda en `reports/entrega_final.pdf`. La ejecucion esperada de las pruebas es `4 passed`.

## Prevencion de fuga

La division train/test ocurre antes del ajuste. `StandardScaler` vive dentro del `Pipeline`, por lo que sus parametros se calculan solamente en cada particion de entrenamiento durante la validacion cruzada.

## Repositorio

https://github.com/oscarinabrazoban-png/INF8239_U01_E01

## Resultados resumidos

El mejor modelo usa kernel RBF, `C=10` y `gamma=0.01`. Su F1 macro promedio en cinco folds es `0.9739`; en prueba obtiene accuracy `0.9825`, F1 `0.9861` y ROC-AUC `0.9977`.

## Advertencia

El ejercicio es academico. El modelo no constituye una herramienta diagnostica ni debe emplearse para decisiones clinicas.