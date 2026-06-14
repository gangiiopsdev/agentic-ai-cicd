from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host.isnumeric():
        args = ['ping', host]
        subprocess.run(args, check=True)
        return {"status": "completed"}
    else:
        return {"error": "Invalid input for ping command"}