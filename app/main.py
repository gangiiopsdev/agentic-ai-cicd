from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    return all(c.isalnum() or c in '.-' for c in host)

@app.get("/ping")
def ping(host: str):
    if is_safe_host(host):
        args = ['ping', host]
        subprocess.run(args, check=True, shell=False)  # Ensuring shell=False to avoid command injection
        return {"status": "completed"}
    else:
        return {"error": "Invalid input"}