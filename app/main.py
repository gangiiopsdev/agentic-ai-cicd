from fastapi import FastAPI
import subprocess

app = FastAPI()

def secure_ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], timeout=5, stderr=subprocess.STDOUT)
        return True, output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return False, e.output.decode('utf-8')

@app.get("/ping")
def ping(host: str):
    success, result = secure_ping(host)
    if success:
        return {"status": "completed", "output": result}
    else:
        return {"status": "error", "output": result}