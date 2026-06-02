from fastapi import FastAPI
import subprocess
def escape_host(host):
    return ''.join(char for char in host if char.isalnum() or char in ['-', '.', '_', ':'])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_host = escape_host(host)
    try:
        output = subprocess.check_output(['ping', '-c 1', safe_host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}