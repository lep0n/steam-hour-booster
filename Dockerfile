FROM python:3.10.5

WORKDIR /home

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY *.py ./
COPY *.json ./
COPY Pipfile ./
COPY Pipfile.lock ./

RUN pip install -U pip pipenv && apt update
RUN pipenv install --deploy --ignore-pipfile

CMD ["pipenv", "run", "python", "main.py"]
