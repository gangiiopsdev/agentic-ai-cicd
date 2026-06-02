from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host):
    return ''.join(c if c.isalnum() or c in ('.', '-', '_') else '_' for c in host)

@app.get("/ping")
def ping(host: str):
    try:
        escaped_host = escape_host(host)
        output = subprocess.run(['ping', '-c', '1', escaped_host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}