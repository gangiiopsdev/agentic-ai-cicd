from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Sanitize input to prevent injection attacks
    safe_host = ''.join(filter(str.isalnum, host))
    try:
        output = subprocess.check_output(['ping', '-c', '1', safe_host], stderr=subprocess.STDOUT, universal_newlines=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)