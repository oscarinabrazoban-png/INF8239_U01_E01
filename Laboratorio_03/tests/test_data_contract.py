import pandas as pd

TARGET = "FORMALIDAD"

REQUIRED = {
    TARGET,
    "REGIÓN",
    "PROVINCIA",
    "RAMA DE ACTIVIDAD",
    "CLASIFICACIÓN MIPYMES"
}


def load_data():
    return pd.read_excel(
        "data/raw/Encuesta-Nacional-a-las-MIPYMES-2023-Base-de-datos.xlsx"
    )


def test_dataset_is_not_empty():
    assert not load_data().empty


def test_required_columns_exist():
    data = load_data()

    data.columns = data.columns.str.strip()

    assert REQUIRED <= set(data.columns)


def test_target_has_no_missing_and_two_classes():
    data = load_data()

    data.columns = data.columns.str.strip()

    y = data[TARGET]

    assert y.notna().all()

    assert y.nunique() >= 2