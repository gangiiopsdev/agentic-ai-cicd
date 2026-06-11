from fastapi import FastAPI
import subprocess
def validate_host(host):
    if host in ['localhost', '127.0.0.1']:
        return True
    else:
        return False
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if validate_host(host):  # Allow only trusted hosts
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    else:
        return {"status": "Invalid host", "error": "Only localhost and 127.0.0.1 are allowed"}