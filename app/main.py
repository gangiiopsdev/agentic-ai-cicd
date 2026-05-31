from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    # Define a list of safe hosts or use a more sophisticated method to validate host input
    return host in ['127.0.0.1', '::1']

@app.get("/"
)
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError("Unsafe host")
    # Secure implementation using subprocess.run with shell=False and check=True to raise an exception if the command fails
    result = subprocess.run(["ping", host], capture_output=True, text=True, check=True)
    return {"status": "completed", "output": result.stdout}