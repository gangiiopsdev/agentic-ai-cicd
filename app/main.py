from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
        return output
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.output}'
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return execute_ping(host)