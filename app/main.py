from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=10)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.output)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)