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
        # Sanitize the host input to prevent command injection
        sanitized_host = subprocess.list2cmdline([host])
        output, _ = execute_command('ping', [sanitized_host])
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}