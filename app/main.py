from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    # Secure implementation
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': e.stderr}