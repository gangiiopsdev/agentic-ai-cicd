from fastapi import FastAPI
import subprocess
gitignore_imports = {"subprocess": None}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.call(["ping", host], shell=False)
    return {"status": "completed"}