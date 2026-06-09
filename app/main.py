from fastapi import FastAPI
import subprocess
from secrets import token_hex
generate_random_hex = lambda: token_hex(5)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if is_safe_hostname(host):
        subprocess.call(['ping', host])  # Use the hostname directly instead of generating a random string
        return {"status": "completed"}
    else:
        return {"error": "Invalid hostname"}