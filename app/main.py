from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_input(input_str):
    try:
        subprocess.check_output(['ping', shlex.quote(input_str)], stderr=subprocess.STDOUT)
        return True
    except subprocess.CalledProcessError as e:
        print(f'Input validation failed: {e}')
        return False

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if validate_input(host):
        try:
            result = subprocess.run(['ping', shlex.quote(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {"status": "completed", "stdout": result.stdout.decode(), "stderr": result.stderr.decode()}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": str(e)}
    else:
        return {"status": "failed", "error": "Invalid input"}