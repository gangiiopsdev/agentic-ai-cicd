from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Use subprocess.run with check_output and shell=False for safer execution
        result = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, universal_newlines=True)
        return result
    except subprocess.CalledProcessError as e:
        return e.output
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return safe_ping(host)