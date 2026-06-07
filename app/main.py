from fastapi import FastAPI
import subprocess
globally_safe_hosts = ['example.com', 'localhost']  # Define a list of safe hosts

def is_host_safe(host):
    return host in globally_safe_hosts

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not is_host_safe(host):
        raise ValueError('Unsafe host')

    subprocess.call(f'ping {host}', shell=False)

    return {"status": "completed"}