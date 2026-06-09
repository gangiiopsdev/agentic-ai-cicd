from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_safe_command(command, *args):
    try:
        result = subprocess.run([command] + list(args), check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):

    # Safe implementation
    command = ["ping", host]
    result = execute_safe_command(*command)

    return {"status": "completed", "output": result}