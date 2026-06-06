from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    result = subprocess.run(args, check=True)
    return {'status': 'completed', 'exit_code': result.returncode}