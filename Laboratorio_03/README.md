# Laboratorio 02 - Condición de la Formalidad de las MIPYMES Dominicanas

## Descripción

Este laboratorio desarrolla un flujo reproducible de ciencia de datos utilizando la Encuesta Nacional a las MIPYMES (ENMIPYMES 2023) del Banco Central de la República Dominicana.

El objetivo es construir un modelo de clasificación supervisada capaz de predecir la condición de formalidad de una empresa a partir de sus características económicas, geográficas y empresariales.

---

## Objetivo

Predecir la variable **FORMALIDAD** utilizando técnicas de Machine Learning y comparar el desempeño de un modelo baseline con un modelo de Máquinas de Vectores de Soporte (SVM).

---

## Dataset

### Nombre

Encuesta Nacional a las MIPYMES (ENMIPYMES 2023)

### Fuente

Banco Central de la República Dominicana

### Unidad de análisis

Micro, pequeña o mediana empresa encuestada.

### Variable objetivo

**FORMALIDAD**

Clases:

- Formal
- Informal

### Tamaño del dataset

- 13,130 observaciones
- 126 variables

---

## Estructura del proyecto

```text
Laboratorio_02
│
├── data
│   ├── raw
│   └── processed
│
├── docs
│   ├── ficha_dataset.md
│   └── procedencia_dataset.md
│
├── notebooks
│   └── Enmipymes_svm.ipynb
│
├── reports
│
├── src
│   └── inf8239_u01
│       ├── __init__.py
│       └── data.py
│
├── tests
│   └── test_data_contract.py
│
├── README.md
├── requirements.txt
└── .gitignore