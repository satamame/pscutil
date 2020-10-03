# pscutil

## Overview

- This is an ongoing project.  
このプロジェクトは開発中です。

## Making environment

### Prerequisite

- You need Python 3.8 and pipenv installed.  
Python 3.8 と pipenv をインストールしておいてください。

### Product

- On the product server, set below os environment variables.  
本番環境では、以下の環境変数を設定してください。
    - DJANGO_SECRET_KEY
        - You can get a new key by get_random_secret_key.py.  
        新しくキーを作るには、get_random_secret_key.py を使います。
    - ALLOWED_HOSTS
        - Comma-separated host names.
- Make virtual environment by `pip install`.  
`pip install` で仮想環境を作ります。

### Development

- In the development environment, you need local_settings.py.  
開発環境では、local_settings.py ファイルが必要です。
    - You can copy and edit local_settings_template.py.  
    local_settings_template.py をコピーして編集してください。
    - Project without local_settings.py is considered as product.  
    local_settings.py ファイルがないと、本番環境と見なされます。
- Make virtual environment by `pip install --dev`.  
`pip install --dev` で仮想環境を作ります。

### Common procedure to start Django

- `python manage.py migrate` in virtual env.
- `python manage.py createsuperuser` in virtual env.
