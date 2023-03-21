# simple django project

## Needed to install

| Program | Version | Links |
| ----------- | ----------- | ----------- |
| Python | 3.10.7 | [link](https://www.python.org/downloads/) |
| Docker | 20.10.22 | [link](https://docs.docker.com/compose/install/) |
| Poetry | 1.3.2 | [link](https://python-poetry.org/docs/#installation) |
| DBeaver | 22.3.4 | [link](https://dbeaver.io/download)

## poetry

```bash
    cd core
    poetry shell
    poetry install
    poetry export -f requirements.txt --output requirements.txt
    poetry run python manage.py runserver
```

## docker

```bash
    docker-compose up -d --build
```
