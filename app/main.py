from fastapi import FastAPI
import subprocess
def run_ping(host):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return output.decode()
    except subprocess.CalledProcessError as e:
        return str(e.output)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return run_ping(host)