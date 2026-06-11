from fastapi import FastAPI
import subprocess
def run_command(command: str):
    result = subprocess.run(command.split(), capture_output=True, text=True)
    return result.stdout, result.stderr
class PingResponse(BaseModel):
    status: str
    output: str
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    command = f"ping {host}"
    stdout, stderr = run_command(command)
    if stderr:
        return PingResponse(status="error", output=stderr)
    else:
        return PingResponse(status="completed", output=stdout)