from fastapi import FastAPI
import subprocess

def generate_safe_command(host):
    return ['ping', host]

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host")
    try:
        result = subprocess.run(generate_safe_command(host), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": str(e)}

def validate_host(host: str) -> bool:
    # Basic validation, more rigorous checks can be added based on requirements
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-:_'
    return all(char in allowed_chars for char in host)