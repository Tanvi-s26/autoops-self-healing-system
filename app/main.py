from fastapi import FastAPI
from prometheus_client import Counter, generate_latest
from fastapi.responses import Response
import random

app = FastAPI()

# Prometheus metric
REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total number of requests"
)

@app.get("/")
def home():
    REQUEST_COUNT.inc()
    return {"message": "AutoOps API is running 🚀"}

@app.get("/health")
def health():
    REQUEST_COUNT.inc()
    return {"status": "healthy"}

@app.get("/simulate-failure")
def simulate_failure():
    REQUEST_COUNT.inc()

    if random.choice([True, False]):
        return {"status": "working fine"}
    else:
        raise Exception("Simulated failure 😈")


# Metrics endpoint for Prometheus
@app.get("/metrics")
def metrics():
    return Response(
        generate_latest(),
        media_type="text/plain"
    )