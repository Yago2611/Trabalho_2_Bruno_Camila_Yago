
from typing import Dict


def write_report(path: str, config: Dict, metrics_values) -> None:
    """ escreve o arquivo de relatorio do experimento """   
    arquivo = open(path,"w")
    for x in config:
        arquivo.write(f"{x}: {config[x]}\n")
    for x in metrics_values:
        arquivo.write(f"{x}: {metrics_values[x]}\n")
    arquivo.close()