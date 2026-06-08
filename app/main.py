from fastapi import FastAPI
import subprocess
def run_ping(host):
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.output}'
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    result = run_ping(host)
    return {'status': 'completed', 'output': result}