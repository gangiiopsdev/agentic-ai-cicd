from fastapi import FastAPI
import subprocess
generate_random_host = lambda: '127.0.0.1'  # Example random host generator
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.call(["ping", generate_random_host()], shell=False)

    return {"status": "completed"}