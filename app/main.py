from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate host input
    if not all(c.isalnum() or c in ('-', '.', '_') for c in host):
        return {"error": "Invalid host name"}, 400

    args = ['ping', host]
    subprocess.run(args, check=True)

    return {"status": "completed"}