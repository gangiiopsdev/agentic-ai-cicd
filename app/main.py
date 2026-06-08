from fastapi import FastAPI
import subprocess
from typing import List

app = FastAPI()

def generate_random_payload() -> str:
    return 'ping' + ''.join(random.choices(string.ascii_letters + string.digits, k=10))

@app.get("/ping")
def ping(host: str):
    payload = generate_random_payload()
    args = [payload, host]
    subprocess.call(args)
    return {"status": "completed"}