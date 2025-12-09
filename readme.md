# Dashboard de População Mundial
**Análise Interativa com Python, Streamlit e Plotly**

## Visão Geral
Este dashboard foi desenvolvido para explorar, visualizar e analisar dados globais de população de forma interativa. Utilizando os streamlit, uma biblioteca do python. Pandas e plotly.express também foram utilizados.
O objetivo principal do dashboard é transformar um dataset bruto em uma ferramenta de análise visual, permitindo insights rápidos.

---

## Por que este dashboard foi desenvolvido?
- Facilitar a análise de dados populacionais.
- Permitir explorar tendências globais, como países mais populosos, distribuição por continente e taxas de crescimento.
- Criar uma ferramenta prática para aprendizado, ideal para estudos de ciência de dados, dashboards, manipulação de datasets e visualização interativa.
- Servir como base para projetos mais avançados, como análises estatísticas, machine learning ou relatórios executivos.

---

## Tecnologias Utilizadas

### **1. Python**
Linguagem usada para leitura, tratamento e manipulação de dados.

### **2. Pandas**
Usado para carregar e filtrar o dataset:
```python
import pandas as pd
df = pd.read_csv("world_population.csv")
```

### **3. Plotly Express**
Biblioteca de visualização interativa:
```python
fig = px.bar(df, x="Country", y="Population")
```

### **4. Streamlit**
Ferramenta que transforma Python em dashboard web:
```python
import streamlit as st
st.title("Dashboard de População Mundial")
```

---

## Estrutura do Dashboard

### **1. Sidebar Interativa**
Permite selecionar continentes e atualiza os gráficos automaticamente.

### **2. Métricas Globais**
Mostra:
- Total de países filtrados  
- População somada  
- Maior população do dataset

### **3. Gráficos**
- **Top 10 Países Mais Populosos** (gráfico de barras)
- **Distribuição Populacional por Continente** (gráfico de pizza)
- **Crescimento x População** (dispersão com bolhas)

### **4. Tabela Completa**
Mostra os dados filtrados, facilitando buscas e consultas específicas.

---

## Conclusão
Este dashboard transforma dados populacionais em uma plataforma interativa e intuitiva, permitindo análises profundas e rápidas. É ideal para estudos, apresentações, relatórios e evolução para projetos mais complexos.

Para melhorias, você pode adicionar:
- mapa mundial por população  
- comparação por ano  
- análises estatísticas  
