from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        output = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE)
        return output.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e}'

@app.get("/ping")
def ping(host: str):
    if not all(c.isalnum() or c in '-.' for c in host):
        return 'Invalid input'
    return safe_ping(host)