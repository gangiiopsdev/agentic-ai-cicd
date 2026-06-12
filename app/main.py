from fastapi import FastAPI
import subprocess
glom = __import__('glom')

app = FastAPI()

def safe_ping(host):
    try:
        result = glom.glom(subprocess.run(['ping', host], check=True, capture_output=True), ['stdout'])
        return {'status': 'completed', 'output': result}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)