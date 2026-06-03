from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'message': 'Ping command executed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'message': 'Ping command failed', 'error': str(e)}

@app.get("/ping")
def ping_host(host: str):
    return ping(host)