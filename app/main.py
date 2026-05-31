from fastapi import FastAPI
import subprocess
def run_ping(host: str):
    try:
        # Validate host to ensure it's a numeric IP address or hostname
        if not host.isnumeric():
            raise ValueError('Invalid input')
        output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    except ValueError as ve:
        return {'status': 'failed', 'error': str(ve)}

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return run_ping(host)