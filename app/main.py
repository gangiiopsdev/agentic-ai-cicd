from fastapi import FastAPI
import subprocess
g-app = FastAPI()

g@app.get("/ping")
def ping(host: str):
    if not host.isnumeric():
        return {"status": "Invalid input"}
    args = ["ping", host]
    subprocess.run(args, check=True)

    return {"status": "completed"}