from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr.decode('utf-8')}'

@app.get("/ping")
def ping(host: str):
    # Safer implementation
    return safe_ping(host)