from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Safe implementation using subprocess.Popen with shell=False and args parameter
    process = subprocess.Popen(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output.decode(), error.decode()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    result, error = safe_ping(host)
    if error:
        return {'status': 'failed', 'error': error}
    else:
        return {'status': 'completed', 'result': result}