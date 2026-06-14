from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_host(host):
    return shlex.quote(host)

@app.get("/ping")
def ping(host: str):
    try:
        safe_host = escape_host(host)
        output = subprocess.check_output(['ping', '-c', '1', safe_host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}