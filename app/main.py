from fastapi import FastAPI
import subprocess
class SanitizedInput:
    @staticmethod
def is_safe(host):
        return host.strip().replace('.', '_').isalnum()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not SanitizedInput.is_safe(host):
        raise ValueError("Invalid input")
    subprocess.call(['ping', host])
    return {"status": "completed"}