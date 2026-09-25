from pathlib import Path
import pandas as pd

def download_dataset(
    url: str,
    destination="data/raw/Encuesta-Nacional-a-las-MIPYMES-2023-Base-de-datos.xlsx.xlsx"
) -> Path:

    if not url.startswith(("https://", "http://")):
        raise ValueError(
            "La fuente debe ser una URL HTTP(S)"
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