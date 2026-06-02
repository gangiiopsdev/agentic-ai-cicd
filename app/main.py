from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_shell_argument(arg):
    return ' '.join(shlex.quote(a) for a in arg.split())

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with check=True and capturing output
    try:
        result = subprocess.run(['ping', escape_shell_argument(host)], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}