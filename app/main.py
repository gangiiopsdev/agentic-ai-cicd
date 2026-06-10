from fastapi import FastAPI
import re
import shlex

app = FastAPI()

def ping(host: str):
    try:
        # Validate input to ensure it is a valid hostname or IP address
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError("Invalid input")
        # Use subprocess.run with shlex.quote for safer execution
        result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    except ValueError as ve:
        return {"status": "failed", "error": str(ve)}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)