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
Realização de todo processo de ETL (Siga os passos solicitados, preferencialente nas ferramentas recomendadas)
OBS:Lembre que este processo é comumente custoso e complexo, não substime as dificuldades implícitas. 
<br>
<br>


##   MARCO DE ENTREGA PARTE 01 (Até item 9.1)

#### 9.2 ESTATISTICAS, SIZING<br>
##### Estatísticas<br>

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

#### 9.3	APLICAÇAO DE ÍNDICES E TESTES DE PERFORMANCE<br>
    a) Lista de índices, tipos de índices com explicação de porque foram implementados nas consultas 
    b) Performance esperada VS Resultados obtidos
    c) Tabela de resultados comparando velocidades antes e depois da aplicação dos índices (constando velocidade esperada com planejamento, sem indice e com índice Vs velocidade de execucao real com índice e sem índice).
    d) Escolher as consultas mais complexas para serem analisadas (consultas com menos de 2 joins não serão aceitas)
    e) As imagens do Explain devem ser inclusas no trabalho, bem como explicações sobre os resultados obtidos.
    f) Inclusão de tabela mostrando as 10 execuções, excluindo-se o maior e menor tempos para cada consulta e 
    obtendo-se a media dos outros valores como resultado médio final.
<br>

#### 10 Backup do Banco de Dados<br>
        Detalhamento do backup.
        a) Tempo
        b) Tamanho
        c) Teste de restauração (backup)
        d) Tempo para restauração
        e) Teste de restauração (script sql)
        f) Tempo para restauração (script sql)
<br>


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



