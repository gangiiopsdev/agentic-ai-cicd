from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        args = ['ping', '-c', '4', host]
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the input to ensure it contains only allowed characters
    if not all(c.isalnum() or c in '-.' for c in host):
        raise ValueError('Invalid input')
    return safe_ping(host)