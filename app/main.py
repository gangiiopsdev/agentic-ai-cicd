from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    response = execute_ping(host)
    return {'status': 'completed', 'response': response}