# Деплой AgroNaparnik

## Локальная проверка

```powershell
cd C:\Users\Pavel\PycharmProjects\PPS
python -m pip install -r requirements.txt
copy .env.example .env
python manage.py check
python manage.py collectstatic --noinput
python manage.py runserver
```

## Render — команды

**Build command** (без migrate — disk недоступен на этапе build):

```bash
pip install -r requirements.txt && python manage.py collectstatic --noinput
```

или:

```bash
bash build.sh
```

**Start command** (migrate при старте, когда disk смонтирован):

```bash
python manage.py migrate --noinput && gunicorn config.wsgi:application --bind 0.0.0.0:$PORT
```

или:

```bash
bash start.sh
```

## Environment variables

См. `.env.example`. Минимум для prod:

- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG=0`
- `DJANGO_ALLOWED_HOSTS=agronaparnik.onrender.com,xn--80aaak1amrcfmhf.xn--p1ai,www.xn--80aaak1amrcfmhf.xn--p1ai`
- `CSRF_TRUSTED_ORIGINS=https://agronaparnik.onrender.com,https://xn--80aaak1amrcfmhf.xn--p1ai,https://www.xn--80aaak1amrcfmhf.xn--p1ai`
- `SQLITE_DB_NAME=data/db.sqlite3` (с persistent disk)

## Persistent Disk

- Mount path: `/opt/render/project/src/data`
- Size: 1 GB

## После деплоя

```bash
python manage.py createsuperuser
```
