FROM python:3.11-alpine

WORKDIR /app

COPY reqs.txt /app/
RUN pip install --no-cache-dir -r reqs.txt

COPY app/ /app/

COPY entrypoint.sh /app/entrypoint.sh

RUN chmod +x /app/entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["sh", "/app/entrypoint.sh"]