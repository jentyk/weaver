FROM python:3.12

WORKDIR /app

COPY flaskr ./flaskr
COPY Pipfile* ./

RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --system

HEALTHCHECK --interval=5m --timeout=3s \
  CMD curl -f http://127.0.0.1/health || exit 1

EXPOSE 8080

ENTRYPOINT ["gunicorn", "-w", "4", "--bind", "0.0.0.0:8080", "flaskr:app"]
