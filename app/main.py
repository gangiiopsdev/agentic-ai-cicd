from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):

    # Secure implementation
    result = safe_ping(host)

    return {"status": "completed", "result": result}