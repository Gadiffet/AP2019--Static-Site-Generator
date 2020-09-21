FROM python:3.8.4

COPY requirement.txt .
RUN pip install -r requirement.txt

WORKDIR /src

COPY . /src

EXPOSE 8000
CMD ["sh", "docker_start.sh"]