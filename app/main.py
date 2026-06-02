from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_input(input_str):
    try:
        args = ['ping', shlex.quote(input_str)]
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True, result.stdout.decode(), result.stderr.decode()
    except subprocess.CalledProcessError as e:
        print(f'Input validation failed: {e}')
        return False, None, str(e)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    is_valid, stdout, stderr = validate_input(host)
    if is_valid:
        return {
            "status": "completed",
            "stdout": stdout,
            "stderr": stderr
        }
    else:
        return {
            "status": "failed",
            "error": "Invalid input"
        }