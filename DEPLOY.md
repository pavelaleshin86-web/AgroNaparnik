# Деплой PPS Studio

## Локальная проверка перед деплоем

```powershell
cd C:\Users\Pavel\PycharmProjects\PPS
python -m pip install -r requirements.txt
copy .env.example .env
python manage.py check
python manage.py test pages
python manage.py collectstatic --noinput
python manage.py runserver
```

## Деплой на Render

1. Создайте репозиторий на GitHub и запушьте проект (без `.env` и `db.sqlite3`).
2. На [render.com](https://render.com): **New → Blueprint** (если используете `render.yaml`) или **New Web Service**.
3. **Build command:**
   ```bash
   ./build.sh
   ```
4. **Start command:**
   ```bash
   gunicorn config.wsgi:application --bind 0.0.0.0:$PORT
   ```
5. **Environment variables** (из `.env.example`):
   - `DJANGO_SECRET_KEY` — сгенерировать длинную случайную строку
   - `DJANGO_DEBUG=0`
   - `DJANGO_ALLOWED_HOSTS=your-app.onrender.com`
   - `CSRF_TRUSTED_ORIGINS=https://your-app.onrender.com`
   - `CONTACT_NOTIFY_EMAIL` — ваш email для заявок
   - SMTP: `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_USE_SSL`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`
6. **Persistent Disk** (для SQLite):
   - Mount path: `/opt/render/project/src/data`
   - В env добавьте: `SQLITE_DB_NAME=data/db.sqlite3`
7. После первого деплоя откройте **Shell** на Render:
   ```bash
   python manage.py createsuperuser
   ```

## Post-deploy checklist

- [ ] Главная, about, services, portfolio, contact — HTTP 200
- [ ] CSS и favicon загружаются
- [ ] Форма контактов сохраняет заявку в `/admin/pages/contactmessage/`
- [ ] Email-уведомление приходит (если SMTP настроен)
- [ ] HTTPS без ошибок mixed content
- [ ] Замените placeholder-контакты в шаблонах на реальные

## Замена контактов

Обновите в шаблонах:
- `templates/base.html` — footer email
- `templates/pages/contact.html` — email, Telegram, телефон
- `.env` / Render env — `CONTACT_NOTIFY_EMAIL`, `DEFAULT_FROM_EMAIL`
