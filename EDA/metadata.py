import hashlib
from pathlib import Path
import pandas as pd


def salvar_metadados_ingestao(caminho_csv: str, df: pd.DataFrame):
    import json
    from datetime import datetime
    """
    Salva um .json ao lado do CSV com metadados da ingestão.
    Substitui o controle manual de versão (V1, V2, V3...).
    """
    arquivo = Path(caminho_csv)
    hash_md5 = hashlib.md5(arquivo.read_bytes()).hexdigest()

    metadados = {
        "arquivo": arquivo.name,
        "hash_md5": hash_md5,
        "data_ingestao": datetime.now().isoformat(),
        "linhas": df.shape[0],
        "colunas": df.shape[1],
        "colunas_lista": list(df.columns),
        "nulos_por_coluna": df.isnull().sum().to_dict(),
    }

    caminho_meta = arquivo.with_suffix('.meta.json')
    with open(caminho_meta, 'w', encoding='utf-8') as f:
        json.dump(metadados, f, ensure_ascii=False, indent=2)

    print(f"Metadados salvos em: {caminho_meta.name}")
    return metadados
