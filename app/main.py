from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.stderr}'

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    if output.startswith('Ping'):  # Check if the output starts with 'Ping' to confirm it's a valid ping response
        return {'status': 'completed', 'output': output}
    else:
        return {'status': 'failed'}