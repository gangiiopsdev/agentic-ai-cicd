from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    try:
        output = subprocess.check_output(['ping', '-c', '4', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)