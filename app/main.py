from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host to ensure it does not contain any unexpected characters or patterns that could be used for injection
    if any(char in host for char in [';', '&', '|', '>', '<', '`', '$', '\']):
        return {'error': 'Invalid input'}, 400
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}