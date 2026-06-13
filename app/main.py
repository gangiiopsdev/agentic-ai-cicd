from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping_safe(host):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, universal_newlines=True)
        return output.strip()
    except subprocess.CalledProcessError as e:
        return str(e.output).strip()

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    result = ping_safe(host)
    return {"status": "completed", "result": result}