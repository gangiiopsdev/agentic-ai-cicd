from fastapi import FastAPI
import subprocess

def safe_ping(host):
    if not all(c.isalnum() or c == '.' for c in host):  # Ensure host contains only alphanumeric characters and dots
        return "Invalid hostname"
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return f"Ping successful: {result.stdout.decode()}", f"Error: {result.stderr.decode()}"
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)