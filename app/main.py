from fastapi import FastAPI
import subprocess
host = 'example.com'  # Replace with actual host
ping_command = ['ping', '-c', '4', host]
call_command = subprocess.Popen(ping_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, error = call_command.communicate()
if call_command.returncode != 0:
    raise Exception(f'Ping failed with return code: {call_command.returncode}')
return {'status': 'completed'}