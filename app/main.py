from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Use subprocess.Popen instead of subprocess.call and avoid using shell=True
    ping_process = subprocess.Popen(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = ping_process.communicate()
    if error:
        raise Exception(f'Ping failed with error: {error.decode()}')
    return output.decode()

@app.get("/ping")
def ping(host: str):
    try:
        result = safe_ping(host)
        return {'status': 'completed', 'output': result}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}