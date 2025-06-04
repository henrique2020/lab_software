# 🚀 API Back-End em Python com FastAPI + Uvicorn + MySQL

Este projeto é uma API RESTful desenvolvida em Python utilizando o framework FastAPI. A API se conecta a um banco de dados MySQL para realizar operações de leitura e escrita.

## 📦 Bibliotecas necessárias

Instale todas as dependências pelo comando `pip install -r requirements.txt` ou instale separadamente as bibliotecas abaixo

* bcrypt
* fastapi
* mysql.connector
* python-dotenv
* python-jose[cryptography]
* uvicorn

## 🧠 Estrutura do Projeto

```
.
├── python-api/
│   ├── dao/
│   │   ├── Database.py
│   │   ├── ExemploDAO.py
│   │   └── ...
│   ├── model/
│   │   ├── Exemplo.py
│   │   └── ...
│   ├── main.py
│   ├── middleware.py
│   ├── routes.py
│   ├── .env
│   └── requirements.txt
└── README.md
```

## ▶️ Execução

```cmd
cd ./python-api
uvicorn main:app --reload
```

| Comando  | Descrição                                                                 |
| -------- | --------------------------------------------------------------------------- |
| --reload | Recarrega automaticamente o servidor em alterações (para desenvolvimento) |
