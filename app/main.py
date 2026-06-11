from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Sanitize input by escaping special characters
        host = subprocess.list2cmdline([host])
        output = subprocess.check_output(['ping', '-c', '1', host], timeout=5, stderr=subprocess.STDOUT)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f"Ping failed with error: {e.output.decode('utf-8')}"

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)