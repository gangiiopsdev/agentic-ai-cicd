from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    # Secure implementation
    args = ['ping', host]
    subprocess.run(args, check=True, text=True, capture_output=True)
    return {'output': result.stdout}