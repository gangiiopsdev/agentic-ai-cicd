from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Safe implementation using subprocess.run
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode()
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.stderr.decode()}'

@app.get("/ping")
def ping(host: str):
    # Use the safe version of ping function
    return {'status': 'completed', 'result': safe_ping(host)}