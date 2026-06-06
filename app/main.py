from fastapi import FastAPI
import subprocess
class Sanitizer:
    @staticmethod
def sanitize_input(input):
        return ''.join(e for e in input if e.isalnum() or e in ('.', '-', '_'))

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    host = Sanitizer.sanitize_input(host)
    args = ['ping', host]
    subprocess.call(args, shell=False)
    return {"status": "completed"}