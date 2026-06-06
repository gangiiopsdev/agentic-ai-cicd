from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.output.decode('utf-8'))

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Validate input to prevent injection attacks
        if not host.replace('.', '').isdigit():
            raise ValueError("Invalid host format")
        return {'status': safe_ping(host)}
    except Exception as e:
        return {'error': str(e)}