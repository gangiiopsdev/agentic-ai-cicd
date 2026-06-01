from fastapi import FastAPI
import shlex
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    args = shlex.split(f"ping {host}")
    subprocess.call(['ping', *args])
    return {"status": "completed"}