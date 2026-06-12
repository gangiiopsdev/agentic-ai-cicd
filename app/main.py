from fastapi import FastAPI
import subprocess
from shlex import quote
import asyncio

app = FastAPI()

def escape_command(user_input):
    return [quote(part.strip()) for part in user_input.split(' ')] if ' ' in user_input else [quote(user_input)]

@app.get("/ping")
def ping(host: str):
    try:
        result = await asyncio.create_subprocess_exec(*escape_command(host), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = await result.communicate()
        if result.returncode != 0:
            raise Exception(f"Ping failed with error: {error.decode('utf-8')}")
        return {"status": "completed", "output": output.decode('utf-8')}
    except Exception as e:
        return {"status": "failed", "error": str(e)}