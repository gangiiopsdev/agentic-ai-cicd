from fastapi import FastAPI
import subprocess
def escape_host(host):
    return ''.join(c if c.isalnum() else '_' for c in host)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run(['ping', '-c', '1', escape_host(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}