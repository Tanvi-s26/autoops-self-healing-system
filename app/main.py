from fastapi import FastAPI
import random

app = FastAPI()

# Home endpoint
@app.get("/")
def home():
    return {"message": "AutoOps API is running 🚀"}


# Health check endpoint (VERY IMPORTANT)
@app.get("/health")
def health():
    return {"status": "healthy"}


# Failure simulation endpoint (VERY IMPORTANT)
@app.get("/simulate-failure")
def simulate_failure():
    if random.choice([True, False]):
        return {"status": "working fine"}
    else:
        raise Exception("Simulated failure 😈")