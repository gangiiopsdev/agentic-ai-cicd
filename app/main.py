from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return str(e.output)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not all(c.isalnum() or c in '.-@' for c in host):
        raise ValueError('Invalid hostname')
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}