from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if all(c.isalnum() or c in ['.', '-'] for c in host):
        try:
            output = subprocess.check_output(['ping', '-c', '1', host], universal_newlines=True)
            return output
        except Exception as e:
            return str(e)

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "result": result}