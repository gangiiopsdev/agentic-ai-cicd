from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error pinging {host}: {e.output}'

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)