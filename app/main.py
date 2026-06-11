from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host):
    # Safe implementation
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    response = run_ping(host)
    return {'status': 'completed', 'response': response}