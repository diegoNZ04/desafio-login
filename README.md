# Desafio Login

Este sistema é um desafio proposto pela Fidelity. Foi desenvolvido em Django, que permite registro e login de usuários.
Ele inclui validações personalizadas e envio de email de boas vindas.

## Tecnologias Utilizadas 

- Django
- SQLite
- Bootstrap + FontAwesome
- SMTP (Gmail)

## Como Executar o Projetp

1. Clonar o Repositório

```
git clone https://github.com/diegoNZ04/desafio-login.git
```

2. Criar e Ativar Um Ambiente Virtual

```
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```

3. Instalar Dependências

```
pip install -r requirements.txt
```

4. Configurar o Banco de Dados

Crie e aplique as migrações:

```
python manage.py migrate
```

5. Executar o Servidor Local

```
python manage.py runserver
```
