
from typing import Dict


def write_report(path: str, config: Dict, metrics_values) -> None:
    """ escreve o arquivo de relatorio do experimento """   
    arquivo = open("data/reports/report.txt","w")
    arquivo.write(f"{path}\n{config}\n{metrics_values}")
    arquivo.close()