from fastapi import FastAPI
import subprocess
get_ip = lambda ping: subprocess.run(['ping', '-c', '1', ping], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = get_ip(host)
    output = result.stdout.decode('utf-8')
    errors = result.stderr.decode('utf-8')
    if errors:
        return {"status": "failed", "error": errors}
    else:
        return {"status": "completed", "output": output}