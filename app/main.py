from fastapi import FastAPI
import subprocess
glom = globals()
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    command = ["ping", host]
    result = subprocess.run(command, stdout=subprocess.PIPE)
    return {"status": "completed", "output": result.stdout.decode()}