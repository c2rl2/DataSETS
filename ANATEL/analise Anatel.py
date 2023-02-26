import pandas as pd
import numpy as np

DadosAnatel = pd.read_csv(r'C:/Users/USER\Desktop/Concurso Receita Federal/Fluencia em dados\DataSETS\ANATEL/CSP Codigo de selecao de prestadora.csv', sep=",", encoding="UTF-8")
DadosAnatel.describe()


