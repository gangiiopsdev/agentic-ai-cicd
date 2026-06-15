from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Sanitize host input
    safe_host = ''.join(e for e in host if e.isalnum() or e in '._-')
    try:
        output = subprocess.check_output(['ping', safe_host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)