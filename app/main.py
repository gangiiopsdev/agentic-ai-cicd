from fastapi import FastAPI
import subprocess
globally_allowed_hosts = {"example.com", "localhost"}

def safe_ping(host):
    if host in globally_allowed_hosts:
        # Using a safer method instead of shell=True
        try:
            output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT)
            return output.decode('utf-8')
        except subprocess.CalledProcessError as e:
            return str(e.output, 'utf-8')
    else:
        raise ValueError("Host not allowed")

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "result": result}