# 🚀 API Back-End em Python com FastAPI + Uvicorn + MySQL

Este projeto é uma API RESTful desenvolvida em Python utilizando o framework FastAPI. A API se conecta a um banco de dados MySQL para realizar operações de leitura e escrita.

## 📦 Bibliotecas necessárias

Instale todoas as dependências pelo comando `pip install -r requirements.txt` ou instale separadamente as bibliotecas abaixo

* bcrypt
* fastapi
* mysql.connector
* python-dotenv
* python-jose[cryptography]
* uvicorn

## 🧠 Estrutura do Projeto

```
.
├── python-app/
│   ├── main.py
│   ├── dao/
│   │   └── database.py
│   ├── model/
│   │   └── exemplo.py
│   ├── routes/
│   ├──.env
│   └── requirements.txt
└── README.md
```

## ▶️ Execução 

`uvicorn app.main:app --reload`

1. app.main 	→ caminho do arquivo main.py dentro do diretório python-app/
2. --reload   		→ recarrega automaticamente o servidor em alterações (para desenvolvimento)
