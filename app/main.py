from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Validate input to prevent command injection
    if host.isalnum() and len(host) < 100:
        command = ['ping', host]
        result = subprocess.run(command, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'invalid_input'}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)