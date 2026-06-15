from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Use subprocess.run for a safer alternative
        args = ['ping', host]
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)