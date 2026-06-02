from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if host in ['localhost', '127.0.0.1']:  # Allow only known safe hosts
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)
    else:
        return 'Invalid host'

@app.get("/ping")
def ping(host: str):
    return {'status': safe_ping(host)}