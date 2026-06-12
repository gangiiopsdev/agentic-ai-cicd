from fastapi import FastAPI
import subprocess
def escape_shell_argument(arg):
    return arg.replace(';', '').replace('&', '').replace('|', '')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        escaped_host = escape_shell_argument(host)
        result = subprocess.run(['ping', '-c', '1', escaped_host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "error": str(e)}
    except Exception as e:
        return {"status": "error", "error": str(e)}