import pytest
from sklearn.datasets import load_breast_cancer
from inf8239_u01.models import build_svm


def test_svm_returns_one_prediction_per_row():
    X, y = load_breast_cancer(return_X_y=True)

    model = build_svm()

    model.fit(X[:450], y[:450])

    assert len(model.predict(X[450:])) == len(X[450:])


def test_svm_rejects_non_positive_c():
    with pytest.raises(ValueError):
        build_svm(C=0)


def test_pipeline_contains_scaler_and_model():
    assert list(build_svm().named_steps) == ["scale", "model"]