from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    try:
        result = subprocess.run(['ping', host], check=True, shell=False, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e}

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    return {'result': 'Pinging host', 'host': host, 'output': ping(host) if ':' in host else 'Invalid input'}