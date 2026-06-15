from fastapi import FastAPI
import ping3

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    response = ping3.ping(host)
    if response is None:
        return {"error": f"Could not reach host: {host}"}
    return {"status": "completed", "response_time": response}