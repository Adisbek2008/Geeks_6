DRF6-54 patched — includes:
- CustomUser (email login) with phone_number, birthdate, first_name, last_name, created_at
- CustomUserManager requires phone_number for superuser
- JWT includes birthdate, first_name, last_name claims
- Redis confirmation utils (save + verify with 5 min TTL)
- IsModerator permission: staff can GET/PUT/PATCH/DELETE others' products but cannot POST
- common.validators.validate_age_for_product_creation enforces 18+ and asks for birthdate
- Celery tasks examples:
    - generate_report_task (call via .delay())
    - scheduled_cleanup_task (for crontab)
    - send_email_task (uses SMTP via Django EMAIL settings)
How to use:
1. clone your repo, replace project files with these or merge.
2. create venv: python3 -m venv venv && source venv/bin/activate
3. pip install -r requirements.txt
4. start redis (docker run -d --name redis -p 6379:6379 redis:7)
5. python3 manage.py makemigrations users product
6. python3 manage.py migrate
7. create superuser via shell to set phone_number:
    from django.contrib.auth import get_user_model
    User = get_user_model()
    User.objects.create_superuser(email='admin@example.com', password='AdminPass123', phone_number='+77770001122')
8. runserver and celery as needed.
