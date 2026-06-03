from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    safe_hosts = ['localhost', '127.0.0.1']
    return host in safe_hosts

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError("Untrusted host")
    result = subprocess.run(['ping', '-c 4', subprocess.check_output(f'echo {host}', shell=True).decode('utf-8').strip()], check=True, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}