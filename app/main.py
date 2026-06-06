from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host):
    try:
        # Using check_output instead of call for better error handling
        result = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return result.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.output)

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)