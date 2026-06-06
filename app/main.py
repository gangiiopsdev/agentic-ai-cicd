from fastapi import FastAPI
import subprocess
global host whitelist
host_whitelist = ['example.com', 'google.com']

app = FastAPI()

def safe_ping(host: str):
    if host not in host_whitelist:
        return "Host not allowed"
    try:
        response = subprocess.run(['ping', host], capture_output=True, text=True, check=True, shell=False)
        return response.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "result": result}