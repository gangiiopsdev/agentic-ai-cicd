from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Use subprocess.Popen safely
    args = ['ping', host]
    process = subprocess.run(args, capture_output=True, text=True, check=False)
    return process.stdout, process.stderr

@app.get("/ping")
def ping(host: str):
    try:
        output, error = safe_ping(host)
        if error:
            return {'status': 'error', 'error': error}
        else:
            return {'status': 'completed', 'output': output}
    except Exception as e:
        return {'status': 'error', 'error': str(e)}