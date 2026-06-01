from fastapi import FastAPI
import subprocess
import shlex

async def validate_and_quote_host(host):
    if not all(c.isalnum() for c in host):
        raise ValueError("Invalid input")
    return shlex.quote(host)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        quoted_host = validate_and_quote_host(host)
        result = await subprocess.run(['ping', '-c', '1', quoted_host], capture_output=True, text=True, check=True)
        return {'result': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': e.stderr}
    except ValueError as e:
        return {'error': str(e)}