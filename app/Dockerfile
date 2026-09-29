FROM cgr.dev/chainguard/python:latest

WORKDIR /app
COPY app.py index.html ./
USER 10001
EXPOSE 8080
ENTRYPOINT ["python", "app.py"]
