from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        result = subprocess.run(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return result.stdout.decode(), None
    except subprocess.CalledProcessError as e:
        return None, str(e)
    except Exception as e:
        return None, str(e)

@app.get("/ping")
def ping(host: str):
    if not host or len(host) > 256:
        return {'status': 'error', 'message': 'Invalid host'}
    output, error = safe_ping(host)
    if error:
        return {'status': 'error', 'message': error}
    else:
        return {'status': 'completed', 'output': output}