from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
        return output
    except subprocess.CalledProcessError as e:
        return str(e.output)

@app.get("/ping")
def ping(host: str):
    result = run_ping(host)
    return {"status": "completed", "output": result}