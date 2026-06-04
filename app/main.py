from fastapi import FastAPI
import subprocess

app = FastAPI()

async def _run_command(command: str, args: list) -> None:
    try:
        result = await asyncio.create_subprocess_exec(*[command] + args,
                                            stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE)
        stdout, stderr = await result.communicate()
        if result.returncode != 0:
            raise Exception(f'Command failed with error: {stderr.decode()}')
    except Exception as e:
        raise Exception(f'Command execution failed: {str(e)}')

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host input
    if not host or len(host) > 256 or not all(c.isalnum() or c in '.-:_[]{}()' for c in host):
        raise Exception('Invalid host input')
    await _run_command('ping', [host])
    return {'status': 'completed'}