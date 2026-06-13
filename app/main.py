from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        ip_parts = host.split('.')
        if len(ip_parts) == 4 and all(part.isdigit() for part in ip_parts) and all(0 <= int(part) <= 255 for part in ip_parts):
            subprocess.call(['ping', '-c', '1', host])
        else:
            raise ValueError('Invalid IP address')
    except Exception as e:
        print(f'Error: {e}')

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}