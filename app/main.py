from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Using check_output instead of call and avoiding shell=True for safety
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f"Failed to ping {host}: {e.output.decode('utf-8')}'

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}