# docker run -it ubuntu bash

FROM python:3.9.6-buster

WORKDIR /app

RUN pip install pipenv

COPY ./Pipfile ./
COPY ./Pipfile.lock ./

RUN pipenv install --system

COPY fast_app ./

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host=0.0.0.0"]