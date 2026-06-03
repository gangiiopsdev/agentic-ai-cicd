from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    ping_command = ['ping', host]
    try:
        result = subprocess.run(ping_command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.stderr}'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)