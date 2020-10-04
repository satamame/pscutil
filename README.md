# pscutil

## Overview

- This is an ongoing project.  
このプロジェクトは開発中です。

## Making environment

### Prerequisite

- You need Python 3.8 and pipenv installed.  
Python 3.8 と pipenv をインストールしておいてください。

### Environment settings

- Create .env file on each environment in the same directory as manage.py is in.  
各環境にて、manage.py と同じディレクトリに .env ファイルを作ります。
    - .env file is not version-controlled.  
    .env ファイルはバージョン管理されません。
    - You can refer to .env_template.  
    .env_template を参考にしてください。
- Run `pipenv install` or `pipenv install --dev`.

### Prepare Django as a service

- `python manage.py migrate` in virtual env.
- `python manage.py createsuperuser` in virtual env.
