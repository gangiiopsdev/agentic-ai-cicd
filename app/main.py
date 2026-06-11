from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return str(e.output)

@app.get="/ping")
def ping(host: str):
    return {'status': 'completed', 'result': safe_ping(host)}