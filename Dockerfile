FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install --no-install-recommends -y python3.8 python3-pip python3-dev libpq-dev
RUN ln -s /usr/bin/pip3 /usr/bin/pip
RUN ln -s /usr/bin/python3.8 /usr/bin/python
RUN pip install --upgrade pip && pip install pipenv

ENV LC_ALL C.UTF-8
ENV LANG en_US.UTF-8

COPY . .
RUN pipenv install --deploy --ignore-pipfile

CMD ["pipenv", "run", "python", "./run.py"]