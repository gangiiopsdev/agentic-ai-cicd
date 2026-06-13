from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        # Use safe shell=True and avoid passing host as part of the arguments list to mitigate shell injection risks
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    return safe_ping(host)