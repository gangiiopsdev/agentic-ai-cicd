from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        # Use subprocess.Popen safely
        process = subprocess.Popen(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        return {'output': output.decode(), 'error': error.decode()}
    except Exception as e:
        return {'error': str(e)}

@app.get="/ping")
def ping(host: str):
    result = safe_ping(host)
    return result