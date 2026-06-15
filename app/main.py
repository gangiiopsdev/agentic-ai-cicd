from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host):
    return host.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        output = subprocess.check_output(['ping', escape_host(host)], stderr=subprocess.STDOUT)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}.