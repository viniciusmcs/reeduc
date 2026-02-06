# REEDUC

## Requisitos
- Python 3.12+
- PostgreSQL 14+

## Ambiente virtual (venv)
```bash
python -m venv venv
venv\Scripts\activate
```

## Dependências
```bash
pip install -r requirements.txt
```

## Variáveis de ambiente
Copie o arquivo de exemplo e ajuste as credenciais:
```bash
copy .env.example .env
```

## Banco de dados (PostgreSQL)
Crie o usuário e o banco:
```bash
psql -U postgres -f scripts/create_db.sql
```

Credenciais solicitadas:
- Usuário: **sejus**
- Senha: **sejus@pi**
- Banco: **reeducdb**

## Migrações
```bash
python manage.py migrate
```

## Executar
```bash
python manage.py runserver
```

## Testes
```bash
python manage.py test
```

## Produção
Defina `DJANGO_SETTINGS_MODULE=reeduc.settings_prod` e `DJANGO_DEBUG=False`.
