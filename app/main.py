from fastapi import FastAPI
import subprocess
from shlex import quote
generate_random_string = lambda: ''.join(random.choices(string.ascii_letters + string.digits, k=16))

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with quoting the host parameter to prevent shell injection
    subprocess.call(['ping', quote(host)])
    return {"status": "completed"}