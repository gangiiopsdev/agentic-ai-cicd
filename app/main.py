from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return result.stdout.decode(), None
    except subprocess.CalledProcessError as e:
        return None, str(e)
    except Exception as e:
        return None, str(e)

@app.get("/ping")
def ping(host: str):
    output, error = safe_ping(host)
    if error:
        return {'status': 'error', 'message': error}
    else:
        return {'status': 'completed', 'output': output}