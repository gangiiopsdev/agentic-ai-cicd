from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    args = ['ping', '-c', '4', host]
    try:
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.stderr.decode('utf-8'))

@app.get("/ping")
def ping(host: str):
    # Validate the host to ensure it contains only allowed characters
    if not all(c.isalnum() or c in '-.' for c in host):
        raise ValueError("Invalid hostname")
    return safe_ping(host)