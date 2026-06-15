from fastapi import FastAPI
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation using shlex.quote to prevent command injection
    subprocess.call(["ping", shlex.quote(host)])
    return {"status": "completed"}