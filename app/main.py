from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Use subprocess.Popen instead of subprocess.call
        args = ['ping', host]
        process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        return {'status': 'completed', 'output': output.decode(), 'error': error.decode() if error else None}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)