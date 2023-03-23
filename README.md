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

## endpoints

| Methods | Permission | Url |
| ----------- | ----------- | ----------- |
| all apps | PublicPermission | [http://127.0.0.1:8000/api/docs/](http://127.0.0.1:8000/api/docs/) |
| redoc apps | PublicPermission | [http://127.0.0.1:8000/api/redoc/](http://127.0.0.1:8000/api/redoc/) |
| user create | AnonPermission | [http://127.0.0.1:8000/api/users/create/](http://127.0.0.1:8000/api/users/create/) |
| user login | AnonPermission | [http://127.0.0.1:8000/api/users/login/](http://127.0.0.1:8000/api/users/login/) |
| user logout | IsAuthenticated | [http://127.0.0.1:8000/api/users/logout/](http://127.0.0.1:8000/api/users/logout/) |
| movies list | PublicPermission | [http://127.0.0.1:8000/api/movies/list/](http://127.0.0.1:8000/api/movies/list/) |
| movies create | SuperuserPermission | [http://127.0.0.1:8000/api/movies/create/](http://127.0.0.1:8000/api/movies/create/) |
| movies update | OwnerPermission | [http://127.0.0.1:8000/api/movies/update/{id}/](http://127.0.0.1:8000/api/movies/update/{id}/) |
| movies detail | SuperuserPermission | [http://127.0.0.1:8000/api/movies/detail/{id}/](http://127.0.0.1:8000/api/movies/detail/{id}/) |
| tag create | PublicPermission | [http://127.0.0.1:8000/api/movies/tag/create/](http://127.0.0.1:8000/api/movies/tag/create/) |
| tag list | PublicPermission | [http://127.0.0.1:8000/api/movies/tags/](http://127.0.0.1:8000/api/movies/tags/) |
| tag movie | PublicPermission | [http://127.0.0.1:8000/api/movies/tagged/{tag}/](http://127.0.0.1:8000/api/movies/tagged/{tag}/) |

1. PublicPermission - available for any requests
2. AnonPermission - available for anonymous requests
3. IsAuthenticated - only logged requests
4. SuperuserPermission - only superuser
5. OwnerPermission - only owner

## postgres
connect to dbeaver

```env
    Host : localhost
    Port : 5433
    Database : simple_app
    Username : simple_app
    Password : django-simple-app
```
