from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return str(e.output)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return {'status': 'completed', 'output': safe_ping(host)}