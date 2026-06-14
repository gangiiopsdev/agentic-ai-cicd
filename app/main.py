from fastapi import FastAPI
import subprocess

generate_command = lambda host: ['ping', '-c', '4', host]

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    subprocess.run(generate_command(host), check=True)
    return {"status": "completed"}

def is_valid_host(host: str) -> bool:
    # Basic validation to ensure the input does not contain any malicious characters
    return all(char.isalnum() or char in ('.', '-') for char in host)