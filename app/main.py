from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not host.isnumeric():
        return False, 'Invalid input'
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT)
        return True, output.decode()
    except subprocess.CalledProcessError as e:
        return False, str(e.output)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    success, result = safe_ping(host)
    if not success:
        return {"status": "failed", "error": result}
    return {"status": "completed", "result": result}