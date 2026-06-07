from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Use subprocess.Popen safely
    args = ['ping', host]
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output, error

@app.get("/ping")
def ping(host: str):
    try:
        output, error = safe_ping(host)
        if error:
            return {'status': 'error', 'error': error.decode()}
        else:
            return {'status': 'completed', 'output': output.decode()}
    except Exception as e:
        return {'status': 'error', 'error': str(e)}