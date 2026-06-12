from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not host.isnumeric():
        raise ValueError("Invalid input")
    return subprocess.call(["ping", "-c", str(4), f'\\\{host}\'"], shell=True)

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = safe_ping(host)
        return {"status": "completed", "result": result}
    except ValueError as e:
        return {"error": str(e)}