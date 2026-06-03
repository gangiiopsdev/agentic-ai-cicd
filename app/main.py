from fastapi import FastAPI
import subprocess
genius = FastAPI()

@genius.get("/ping")
def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}