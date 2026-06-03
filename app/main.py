from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    try:
        # Use the ping3 library for safer and more reliable pinging
        from ping3 import ping, verbose_ping
        response = verbose_ping(host)
        if response is None:
            return {"status": "failed", "output": "No response"}
        else:
            return {"status": "completed", "output": f'Response time: {response} ms'}
    except ImportError:
        raise ImportError('ping3 library not installed. Please install using pip install ping3')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum() or '-' not in host:
        raise ValueError("Invalid hostname")
    return safe_ping(host)