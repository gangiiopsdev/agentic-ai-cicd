from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Sanitize input to prevent command injection
        host = subprocess.list2cmdline([host])
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.output.decode('utf-8')}'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)