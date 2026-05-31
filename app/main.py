from fastapi import FastAPI
import subprocess
def escape_host(host):
    return host.replace(';', '').replace('&', '').replace('|', '')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        output = subprocess.check_output(['ping', escape_host(host)], stderr=subprocess.STDOUT, universal_newlines=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "error": str(e)}