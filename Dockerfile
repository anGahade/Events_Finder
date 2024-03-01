FROM python:3.11-alpine

ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache bash \
    && apk add --no-cache postgresql-dev gcc python3-dev musl-dev

WORKDIR /code

COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/

RUN adduser --disabled-password service-user
USER service-user

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
