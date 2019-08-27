import atexit
import json
import os
import webbrowser
from pathlib import Path
from urllib.request import HTTPError, Request, urlopen

from . import randomize as Randomize
from .commander import Commander
from .layouts import *
from .tracers import *
from .types import PathLike

__all__ = (
    "Randomize", "Commander",
    "Array1DTracer", "Array2DTracer", "ChartTracer", "GraphTracer", "LogTracer", "Tracer",
    "HorizontalLayout", "Layout", "VerticalLayout"
)


def create_json_file(path: PathLike = "./visualization.json"):
    commands = json.dumps(Commander.commands, separators=(",", ":"))
    with Path(path).open("w", encoding="UTF-8") as file:
        file.write(commands)


def get_url() -> str:
    url = "https://algorithm-visualizer.org/api/visualizations"
    commands = json.dumps(Commander.commands, separators=(",", ":")).encode('utf-8')
    request = Request(
        url,
        method="POST",
        data=commands,
        headers={
            "Content-type": "application/json; charset=utf-8",
            "Content-Length": len(commands)
        }
    )
    response = urlopen(request)

    if response.status == 200:
        return response.read().decode('utf-8')
    else:
        raise HTTPError(
            url=url,
            code=response.status,
            msg="Failed to retrieve the scratch URL: non-200 response",
            hdrs=dict(response.info()),
            fp=None
        )


@atexit.register
def execute():
    if os.getenv("ALGORITHM_VISUALIZER"):
        create_json_file()
    else:
        url = get_url()
        webbrowser.open(url)

