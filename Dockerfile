FROM python:3.10-slim as builder
WORKDIR /app
COPY requirements-prod.txt .
RUN pip install --user -r requirements-prod.txt

FROM python:3.10-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY src/ src/
COPY .env.prod .env
ENV PATH=/root/.local/bin:$PATH
ENV PYTHONPATH=/app
CMD ["python", "-m", "src.main"]
