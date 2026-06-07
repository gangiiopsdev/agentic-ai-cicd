from fastapi import FastAPI
import re
def safe_ping(host):
    try:
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
    # Sanitize the input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid hostname")
    # Validate and sanitize the host parameter to prevent potential issues with ping3
    import socket
    try:
        socket.gethostbyname(host)
    except socket.gaierror:
        raise ValueError("Invalid hostname")
    return safe_ping(host)