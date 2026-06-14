from fastapi import FastAPI
import subprocess
def shell_safe(input_string):
    return ''.join(c if c.isalnum() or c in '-_.:/@' else '_' for c in input_string)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_host = shell_safe(host)
    args = ["ping", safe_host]
    result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed", "stdout": result.stdout.decode(), "stderr": result.stderr.decode()}