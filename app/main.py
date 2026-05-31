from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run instead of subprocess.call
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'host': host, 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'host': host, 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)