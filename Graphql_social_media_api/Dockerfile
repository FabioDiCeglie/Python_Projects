FROM python:3.10
ENV PYTHONUNBUFFERED=1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /app/
# CMD /app/docker-entrypoint.sh
RUN chmod +x /app/docker-entrypoint.sh
ENTRYPOINT [ "/bin/sh", "/app/docker-entrypoint.sh" ]
