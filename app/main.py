from fastapi import FastAPI
import subprocess

app = FastAPI()

def _ping(host):
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT)
        return True, output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return False, str(e.output)

@app.get("/ping")
def ping(host: str):
    success, result = _ping(host)
    if success:
        return {"status": "completed", "message": "Ping successful", "output": result}
    else:
        return {"status": "failed", "error": result}