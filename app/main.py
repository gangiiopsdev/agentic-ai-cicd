from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        output = subprocess.run(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if output.returncode == 0:
            return {'status': 'completed', 'output': output.stdout}
        else:
            return {'status': 'failed', 'output': output.stderr}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)