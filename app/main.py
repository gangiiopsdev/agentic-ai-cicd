from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True)
        return output.stdout
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    result = run_ping(host)
    return {'status': 'completed', 'result': result}