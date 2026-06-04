from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: f'ping {host}'
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        output = subprocess.run(generate_ping_command(host), shell=False, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": output.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}