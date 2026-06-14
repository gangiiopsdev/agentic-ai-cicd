from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it does not contain potentially harmful characters
    if any(char in host for char in [';', '&', '|', '`', '&&', '||', '$', '<', '>', '*', '?', '~']):
        return {"error": "Invalid input detected"}
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}