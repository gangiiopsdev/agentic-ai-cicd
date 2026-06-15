from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Using check_output avoids shell=True and is safer
        result = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'result': result.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)