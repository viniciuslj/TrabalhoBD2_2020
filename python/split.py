import sys
from pathlib import Path
import csv
from datetime import datetime, timezone

arq_entrada = sys.argv[1]
dir_saida = sys.argv[2]

local_id = 0
local_dic = {}

responsavel_id = 0
responsavel_dic = {}

tempo_id = 0
tempo_dic = {}

tipo_id = 0
tipo_dic = {}

# carrega os tipos de ocorrência
tipos = {}
tipo_csv = csv.reader(open("tipo.csv", 'r', encoding='utf-8'), delimiter=';')
for row in tipo_csv:
    tipos[row[0]] = row[1]

# cria o diretório de saída
Path(dir_saida).mkdir(parents=True, exist_ok=True)

with open(dir_saida + '/ocorrencia.csv', 'w', newline='', encoding='utf-8') as file_out:
    out_csv = csv.writer(file_out, delimiter=';')
    with open(arq_entrada, 'r', encoding='utf-8') as file_in:
        in_csv = csv.reader(file_in, delimiter=';')
        for row in in_csv:
            
            tipo = row[1] # código do tipo de ocorrência
            if tipo not in tipo_dic:
                tipo_id = tipo_id + 1
                tipo_dic[tipo] = tipo_id
            
            local = row[3] + ';' + row[2] # bairro;cidade
            if local not in local_dic:
                local_id = local_id + 1
                local_dic[local] = local_id
            
            responsavel = row[5] + ';' + row[4] # subunidade;unidade
            if responsavel not in responsavel_dic:
                responsavel_id = responsavel_id + 1
                responsavel_dic[responsavel] = responsavel_id
            
            dt = datetime.strptime(row[7], "%d/%m/%Y %H:%M")
            tempo = "{0};{1};{2};{3};{4}".format(dt.day, dt.weekday(), dt.month, dt.year, dt.hour)
            
            if tempo not in tempo_dic:
                tempo_id = tempo_id + 1
                tempo_dic[tempo] = tempo_id

            row_out = [
                row[0],
                tipo_dic[tipo],
                local_dic[local],
                responsavel_dic[responsavel],
                tempo_dic[tempo],
                1
            ]

            out_csv.writerow(row_out)

# tipo.csv
with open(dir_saida + '/tipo.csv', 'w', encoding='utf-8') as file_out:
    for key, id in tipo_dic.items():
        file_out.write(str(id) + ';' + key + ';' + tipos[key] +'\n')

# local.csv
with open(dir_saida + '/local.csv', 'w', encoding='utf-8') as file_out:
    for key, id in local_dic.items():
        file_out.write(str(id) + ';' + key + '\n')

# responsavel.csv
with open(dir_saida + '/responsavel.csv', 'w', encoding='utf-8') as file_out:
    for key, id in responsavel_dic.items():
        file_out.write(str(id) + ';' + key + '\n')

# tempo.csv
with open(dir_saida + '/tempo.csv', 'w', encoding='utf-8') as file_out:
    for key, id in tempo_dic.items():
        file_out.write(str(id) + ';' + key + '\n')