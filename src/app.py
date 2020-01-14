import json
from pathlib import Path

from configuration import configuration
from environs import Env
from fastapi import FastAPI, Body
from zenroom.zenroom import zencode_exec

app = FastAPI(title="RESTRoom")
env = Env()
env.read_env()

conf_file = env("RESTROOM_CONFIG_FILE")
conf = Path(conf_file).read_text().splitlines()


def make_function(script):
    def _function(data: str = None, keys: str = None):
        print(configuration.registered_middleware)
        configuration.input()
        result = zencode_exec(script=script, keys=keys, data=data)
        configuration.output()
        return {"err": result.stderr, "out": json.loads(result.stdout)}
    return _function


for _ in conf:
    method, route, filename = _.split(" ")
    zencode = Path(filename).read_text()
    app.add_api_route(route,
                      make_function(zencode),
                      methods=[method],
                      description=zencode,
                      summary=zencode,
                      tags=['Zencode'])
