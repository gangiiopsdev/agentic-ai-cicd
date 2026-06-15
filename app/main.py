from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        ip_address = subprocess.check_output(['nslookup', host], stderr=subprocess.STDOUT).decode('utf-8').splitlines()[2].split()[3]
        result = subprocess.run(['ping', '-c', '1', ip_address], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)