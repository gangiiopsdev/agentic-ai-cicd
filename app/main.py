from fastapi import FastAPI
import subprocess

app = FastAPI()

def quote_host(s):
    return ''.join(c if c.isalnum() or c in '-.' else '_' for c in s)

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent injection attacks
    if not host.isalnum():
        return {"status": "failed", "error": "Invalid host name"}
    try:
        output = subprocess.check_output(['ping', '-c', '1', quote_host(host)], stderr=subprocess.STDOUT, text=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}