from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]

def download_dataset(
    url: str,
    destination=None
) -> Path:

    if not url.startswith(("https://", "http://")):
        raise ValueError(
            "La fuente debe ser una URL HTTP(S)"
        )

    if destination is None:
        destination = (
            PROJECT_ROOT
            / "data"
            / "raw"
            / "Encuesta-Nacional-a-las-MIPYMES-2023-Base-de-datos.xlsx"
        )


    path = Path(destination)

    path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    frame = pd.read_excel(url)

    if frame.empty:
        raise ValueError(
            "El dataset descargado está vacío"
        )

    frame.to_excel(
        path,
        index=False
    )

    return path