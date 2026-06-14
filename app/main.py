from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host):
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    output = run_ping(host)
    return {'status': 'completed', 'output': output}