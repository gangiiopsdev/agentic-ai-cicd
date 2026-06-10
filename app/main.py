from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Safer implementation using Popen with shell=False and complete command path
        result = subprocess.Popen(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
        output, error = result.communicate()
        return {'status': 'completed', 'output': output.decode(), 'error': error.decode() if error else None}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)