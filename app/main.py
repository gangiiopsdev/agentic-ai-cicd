from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_command(command, arguments):
    process = subprocess.Popen([command] + arguments, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output.decode(), error.decode()

@app.get("/ping")
def ping(host: str):
    try:
        output, _ = execute_command('ping', [host])
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}