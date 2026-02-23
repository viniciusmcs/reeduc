# REEDUC

## Requisitos
- Python 3.12+

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

## Migrações
```bash
python manage.py migrate
```

## Banco de dados (SQLite padrão)
O projeto está configurado para usar `sqlite3` por padrão:

```python
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': BASE_DIR / 'db.sqlite3',
	}
}
```

Se quiser PostgreSQL, defina `USE_SQLITE=False` no `.env` e configure `DB_*`.

## Criar superusuario
```bash
python manage.py createsuperuser
```

## Executar
```bash
python manage.py runserver
```

## Acesso na rede interna (HTTP)
O sistema pode ser acessado na rede por:

`http://10.0.125.4:8000`

Para subir escutando no IP da máquina:

```bash
python manage.py runserver 0.0.0.0:8000
```

## Testes
```bash
python manage.py test
```

## Produção
Defina `DJANGO_SETTINGS_MODULE=reeduc.settings_prod` e `DJANGO_DEBUG=False`.

Neste projeto, o `settings_prod` está ajustado para rede interna por HTTP (sem redirecionamento obrigatório para HTTPS).
