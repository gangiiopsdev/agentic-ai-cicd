from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.strip() or any(char in host for char in ' ;&*?^%$#@!+={}[]|\<>,.?/~`'):
        raise HTTPException(status_code=400, detail="Invalid hostname")
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}