# TrabalhoBD2_2020


# TRABALHO 01 : Ocorrências Policiais Da Grande Vitória
<br>
Trabalho desenvolvido durante a disciplina de BD2
 
# Sumário

### 1	COMPONENTES
<br>
Vinícius - 20101BSI0615
<br>

### 2	Escolha da base de dados e explicação sobre informações relacionadas
<br>
Ocorrências policiais da Grande Vitória resgistradas nos anos de 2014 e 2015.<br>
Fonte: SESP - Secretaria de Estado da Segurança Pública e Defesa Social
<br>

### 3 Fast Imersion Canvas
<br>

![Fast Imersion Canvas](https://github.com/viniciuslj/TrabalhoBD2_2020/blob/main/img/modelos/Fast%20Immersion%20Canvas.png)<br>
Link do DOCS: https://docs.google.com/presentation/d/14wGFh0xtsRG9IIhV1w6O_9XpKqbQICGXFUXmwtUdzOk/edit?usp=sharing<br>
<br>

### 4 Fast Modelling Canvas
<br>

![Fast Modelling Canvas](https://github.com/viniciuslj/TrabalhoBD2_2020/blob/main/img/modelos/Fast%20Modelling%20Canvas.png)<br>
Link do DOCS: https://docs.google.com/presentation/d/1IRQFbgwR4U8392uU6h7c7p4xZBYW11HkGwRWeOXxwJ8/edit?usp=sharing<br>
<br>

### 5 Fast EDA e PPD Canvas
<br>
Inclusão do Fast EDA Canvas, Fast PPD Canvas + Inclusão de Pré processamentoe e Análise exploratoria de dados (Jupyter notebook/Colab)
<br>
<br>

### 6 Mapa de ETL
<br>
Inclusão do Mapa de ETL
<br>
<br>
     
### 7	MODELO CONCEITUAL, LOGICO E FISICO - OLTP
<br>

![Modelo OLTP](https://github.com/viniciuslj/TrabalhoBD2_2020/blob/main/img/modelos/modelo-oltp.png)<br>
SQL de Criação: https://github.com/viniciuslj/TrabalhoBD2_2020/blob/main/sql/create-oltp.sql<br>
<br>

### 8	MODELO CONCEITUAL, LOGICO E FISICO - OLAP
<br>

![Modelo OLAP](https://github.com/viniciuslj/TrabalhoBD2_2020/blob/main/img/modelos/modelo-olap.png)<br>
SQL de Criação: https://github.com/viniciuslj/TrabalhoBD2_2020/blob/main/sql/create-olap.sql<br>
<br>
 
### 9 CARGA DE DADOS,ANÁLISE DE METADADOS,ESTATISTICAS, SIZING E INDEXAÇÃO
#### 9.1	CARGA DE DADOS A ANÁLISE DOS RESULTADOS OBTIDOS 
<br>
O processo de carga foi realizado por meio de script Python. O script gera arquivos CSV das
dimensões tendo como base os dados de entrada. Os arquivos CSV são carregados para a base OLAP
utilizando a instrunção SQL COPY.

<br>

##### Script Python 
<br>

<b>Execução:</b>
<br>

```shell
py split.py arquivo-entrada.cvs <diretório-saida>
```

Script Python: https://github.com/viniciuslj/TrabalhoBD2_2020/blob/main/python/split.py<br>

<br>

##### SQL
<br>

```sql
-- Local
COPY local(id, bairro, cidade)
FROM 'C:\ocorrencias\dados\local.csv'
DELIMITER ';' CSV;

-- Responsável
COPY responsavel(id, subunidade, unidade)
FROM 'C:\ocorrencias\dados\responsavel.csv'
DELIMITER ';' CSV;

-- Tipo
COPY tipo(id, codigo, descricao)
FROM 'C:\ocorrencias\dados\tipo.csv'
DELIMITER ';' CSV;

-- Tempo
COPY tempo(id, dia, dia_semana, mes, ano, hora)
FROM 'C:\ocorrencias\dados\tempo.csv'
DELIMITER ';' CSV;

-- Ocorrência
COPY ocorrencia(id,tipo_id,local_id,responsavel_id,tempo_id,quantidade)
FROM 'C:\ocorrencias\dados\ocorrencia.csv'
DELIMITER ';' CSV;

```

<br>

##   MARCO DE ENTREGA PARTE 01 (Até item 9.1)

#### 9.2 ESTATISTICAS, SIZING<br>
##### Estatísticas do banco de dados OLAP<br>

```sql
analyse local;
analyse tipo;
analyse tempo;
analyse responsavel;
analyse ocorrencia;

select schemaname, tablename, attname, null_frac, avg_width, n_distinct, most_common_vals, correlation
from pg_stats
where schemaname = 'public';
```

<br>

![Estatísticas](https://github.com/viniciuslj/TrabalhoBD2_2020/blob/main/img/estatisticas.png)<br>
<br>

##### Sizing do banco de dados OLAP<br>

```sql
select 
	c.relname as "relation", 
	relkind as "tipo_estrutura",
	pg_size_pretty(pg_relation_size(c.oid)) as "size object",
	pg_size_pretty(pg_total_relation_size(c.oid)) as "total size",
	n_live_tup as "registros"
from pg_class c
	left join pg_namespace n on (n.oid = c.relnamespace)
	left join pg_stat_user_tables t on (t.relid = c.oid)
where nspname not in ('pg_catalog', 'information_schema')
  and nspname !~'^pg_toast'
order by pg_total_relation_size(c.oid) desc;
```

<br>

![Sizing](https://github.com/viniciuslj/TrabalhoBD2_2020/blob/main/img/sizing.png)<br>
<br>

#### 9.3	APLICAÇAO DE ÍNDICES E TESTES DE PERFORMANCE<br>

Foram criados índices BTREE nos campos da tabela de ocorrências. Foi necessário aumentar a quantidade de ocorrências de 379143 para 1.084.732, incluíndo os anos de 2015 e 2016. Duas consultas foram executadas para análise, porém não foram alcançadas grandes diferenças para a quantidade de registros.
<br>

##### Grão <br>

```sql
select 
	oc.id, 
	tp.codigo, tp.descricao, 
	re.subunidade, re.unidade,
	lo.bairro, lo.cidade, 
	te.hora, te.dia, te.mes, te.ano, te.dia_semana
from ocorrencia oc
inner join tipo tp on tp.id = tipo_id
inner join responsavel re on re.id = responsavel_id
inner join local lo on lo.id = local_id
inner join tempo te on te.id = tempo_id
order by oc.id;
```

<br> 

##### Crimes contra Patrimônio ou Pessoa	

<br>

```sql
select 
	oc.id, 
	tp.codigo, tp.descricao, 
	re.subunidade, re.unidade,
	lo.bairro, lo.cidade, 
	te.hora, te.dia, te.mes, te.ano, te.dia_semana
from ocorrencia oc
inner join tipo tp on tp.id = tipo_id
inner join responsavel re on re.id = responsavel_id
inner join local lo on lo.id = local_id
inner join tempo te on te.id = tempo_id
where tp.codigo like 'B%' or tp.codigo like 'A%'
order by oc.id;
```

<br>

##### Resultados <br>

<br>

![Sizing](https://github.com/viniciuslj/TrabalhoBD2_2020/blob/main/img/resultados-idx.png)<br>

<br>

##### 

#### 10 Backup do Banco de Dados<br>

##### PG_DUMP <br>

Foi executado em 1.367 segundo. Gerando um arquivo de 2.17 MB.<br>

```python
import os, time

t_inicio = time.time()
os.system('pg_dump --verbose -Fc --file=ocorrencias_db.dump postgres://postgres:123456@localhost:5432/ocorrencias_db')
t_fim = time.time()

print("---")
print("pg_dump em %s segundos" % (t_fim - t_inicio))
```

<br>

![PG_DUMP](https://github.com/viniciuslj/TrabalhoBD2_2020/blob/main/img/pgdump.png)<br>

##### PG_RESTORE

Foi executado em 1.694 segundo.<br>

```python
import os, time

t_inicio = time.time()
os.system('pg_restore --verbose -d "postgres://postgres:123456@localhost:5432/ocorrencias_db" ocorrencias_db.dump')
t_fim = time.time()

print("---")
print("pg_restore em %s segundos" % (t_fim - t_inicio))
```

<br>

![PG_RESTORE](https://github.com/viniciuslj/TrabalhoBD2_2020/blob/main/img/pgrestore.png)<br>

![Testes](https://github.com/viniciuslj/TrabalhoBD2_2020/blob/main/img/teste-restore.png)<br>

### 11 MINERAÇÃO DE DADOS

a) Tópicos introdutórios
* Explicação/Fundamentação teórica sobre o método, objetivos e restrições! (formato doc/odt ou PDF)
* Onde/quando aplicar 
> ##### Estudar e explicar artigo que aplique o método de mineração de dados/machine learning escolhido
* exemplo de uso/aplicação 
> ##### Implementar algoritmo básico de exemplo obtido na literatura (enviar código executável junto do trabalho com detalhamento de explicação para uso passo a passo)
b) Aplicação de data mining/machine learning nos dados do trabalho 
* definir conjunto de dados relevante para o processo
* proposta deve ser aprovada pelo professor (deve ser enviada para avaliação até 72 hora antes da entrega da atividade)

Referência: http://scikit-learn.org/stable/index.html
<br>
Referências adicionais:
Scikit learning Map : http://scikit-learn.org/stable/tutorial/machine_learning_map/index.html
Machine learning in Python with scikit-learn: https://www.youtube.com/playlist?list=PL5-da3qGB5ICeMbQuqbbCOQWcS6OYBr5A


##   MARCO DE ENTREGA PARTE 02 (Até item 11)



### 12 CRIAÇÃO DOS SLIDES E VÍDEO PARA APRESENTAÇAO FINAL <br>

#### a) Conclusão análises de data mining/dashboards e ajustes no trabalho (conforme ajustes solicitados pelo professor)
#### b) Criação de Slides para apresentação dos resultados provenientes do banco de dados OLAP desenvolvido (CANVAS + NOTEBOOKS E CONCLUSÕES)
#### c) Modelo Pecha Kucha(Apresentação com tempo de  6m40s) 
#### OBS: Esta é uma atividade de grande relevância no contexto do trabalho. Mantenha o foco nos principais resultados.


##   MARCO DE ENTREGA PARTE 03 (Até item 12)

### 13  FORMATACAO NO GIT: https://help.github.com/articles/basic-writing-and-formatting-syntax/
<comentario no git>
    
##### About Formatting
    https://help.github.com/articles/about-writing-and-formatting-on-github/
    
##### Basic Formatting in Git
    
    https://help.github.com/articles/basic-writing-and-formatting-syntax/#referencing-issues-and-pull-requests
    
    
##### Working with advanced formatting
    https://help.github.com/articles/working-with-advanced-formatting/
#### Mastering Markdown
    https://guides.github.com/features/mastering-markdown/

### OBSERVAÇÕES IMPORTANTES

#### Todos os arquivos que fazem parte do projeto (Imagens, pdfs, arquivos fonte, etc..), devem estar presentes no GIT. Os arquivos do projeto vigente não devem ser armazenados em quaisquer outras plataformas.
1. Caso existam arquivos com conteúdos sigilosos, comunicar o professor que definirá em conjunto com o grupo a melhor forma de armazenamento do arquivo.

#### Todos os grupos deverão fazer Fork deste repositório e dar permissões administrativas ao usuário deste GIT, para acompanhamento do trabalho.

#### Os usuários criados no GIT devem possuir o nome de identificação do aluno (não serão aceitos nomes como Eu123, meuprojeto, pro456, etc). Em caso de dúvida comunicar o professor.


Link para BrModelo:<br>
http://sis4.com/brModelo/brModelo/download.html
<br>


Link para curso de GIT<br>
![https://www.youtube.com/curso_git](https://www.youtube.com/playlist?list=PLo7sFyCeiGUdIyEmHdfbuD2eR4XPDqnN2?raw=true "Title")



