FROM python:3.7

RUN apt-get update
RUN apt-get install -y \
    postgresql-client \
    sqlite3 \
  && rm -fr /var/lib/apt/lists/* \
  && mkdir -p /usr/AIDjangoWebApp

WORKDIR /usr/AIDjangoWebApp
COPY . /usr/AIDjangoWebApp
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8005

ENTRYPOINT ["python", "manage.py"]

CMD ["runserver", "0.0.0.0:8005"]