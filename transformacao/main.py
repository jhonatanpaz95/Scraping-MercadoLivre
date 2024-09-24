import pandas as pd
import sqlite3
from datetime import datetime

# ler arquivo json

df = pd.read_json(r'C:\Users\Samsung\Desktop\projetos\Scraping-MercadoLivre\coleta\data.jsonl', lines=True)


df['source'] = 'https://lista.mercadolivre.com.br/tenis-esportivo'
df['data_coleta'] = datetime.now()

#Tratar os valores nulos para colunas numéricas e de texto
df['old_price_reais'] = df['old_price_reais'].fillna(0).astype(float)
df['old_price_centavos'] = df['old_price_centavos'].fillna(0).astype(float)
df['new_price_reais'] = df['new_price_reais'].fillna(0).astype(float)
df['new_price_centavos'] = df['new_price_centavos'].fillna(0).astype(float)
df['reviews_rating_number'] = df['reviews_rating_number'].fillna(0).astype(float)

# Remover paênteses das colunas do 'reviews_amount'
try:
    df['reviews_amount'] = df['reviews__amount'].str.replace('[\(\)]', '', regex=True)
    df['reviews_amount'] = df['reviews__amount'].fillna(0).astype(int)
    if False:
        pass
except Exception as e:
    print(e)


# tratar os preços como floats e calcular os valores totais
df['old_price'] = df['old_price_reais'] + df['old_price_centavos'] / 100
df['new_price'] = df['new_price_reais'] + df['new_price_centavos'] / 100

# Remover as colunas antigas com preços
df.drop(columns=['old_price_reais', 'old_price_centavos', 'new_price_reais', 'new_price_reais'])

# Conectar ao banco de dados SQLite
conn = sqlite3.connect(r'C:\Users\Samsung\Desktop\projetos\Scraping-MercadoLivre\coleta\quotes.db')

# Salvar o DataFrame no banco de dados SQLite
df.to_sql('mercadolivre_items', conn, if_exists='replace',index=False)

# Fechar a conexão com o banco de dados
conn.close()

print(df.head())