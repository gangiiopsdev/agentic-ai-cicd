from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    args = ['ping', host]
    return subprocess.run(args, check=True)

def validate_input(input_str: str) -> bool:
    if not input_str.isalnum() or '&&' in input_str or ';' in input_str:
        return False
    return True

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not validate_input(host):
        return {"error": "Invalid input"}, 400
    result = safe_ping(host)
    return {"status": "completed", "output": result.stdout}