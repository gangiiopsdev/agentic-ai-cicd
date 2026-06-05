from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_host = host.replace(';', '').replace('&', '').replace('\', '')
    try:
        output = subprocess.check_output(['ping', safe_host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'result': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output.decode('utf-8')}"