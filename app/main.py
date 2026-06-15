from fastapi import FastAPI
import subprocess
def run_ping(host):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.output)
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    result = run_ping(host)
    return {'status': 'completed', 'result': result}