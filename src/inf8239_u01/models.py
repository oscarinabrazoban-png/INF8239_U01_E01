from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC


def build_svm(C=1.0, gamma="scale"):
    if C <= 0:
        raise ValueError("C debe ser positivo")

    return Pipeline([
        ("scale", StandardScaler()),
        (
            "model",
            SVC(
                C=C,
                gamma=gamma,
                kernel="rbf",
                probability=True,
                random_state=42
            )
        )
    ])