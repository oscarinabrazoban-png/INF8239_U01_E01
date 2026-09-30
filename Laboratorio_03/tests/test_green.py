from pathlib import Path
import sys

sys.path.append(
    str(
        (Path(__file__).resolve().parents[1] / "src")
    )
)
import pandas as pd

from inf8239_u01.green import pareto_flags


def test_pareto_marks_dominated_rows():

    df = pd.DataFrame({
        "f1_macro": [0.90, 0.90, 0.88],
        "fit_median_s": [2.0, 1.0, 3.0]
    })

    assert pareto_flags(df) == [
        False,
        True,
        False
    ]


def test_single_model_is_pareto():

    df = pd.DataFrame({
        "f1_macro": [0.80],
        "fit_median_s": [1.0]
    })

    assert pareto_flags(df) == [
        True
    ]