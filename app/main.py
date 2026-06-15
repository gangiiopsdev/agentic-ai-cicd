from fastapi import FastAPI
import subprocess
def escape_shell_arg(arg):
    return ''.join(c if c.isalnum() else f'\{c}' for c in arg)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.strip():
        return {"error": "Host is required and cannot be empty."}
    args = ["ping", escape_shell_arg(host)]
    result = subprocess.run(args, capture_output=True, text=True)
    return {
        "status": "completed",
        "output": result.stdout,
        "stderr": result.stderr
    }