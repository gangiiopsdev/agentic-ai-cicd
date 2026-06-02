from fastapi import FastAPI
import subprocess
gen_ip = lambda x: x.replace(';', '').replace('|', '')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to avoid command injection
    sanitized_host = gen_ip(host)
    subprocess.call(f'ping {sanitized_host}', shell=True)
    return {"status": "completed"}