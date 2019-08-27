import atexit
import json
import os
import webbrowser
from pathlib import Path

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
    import requests

    commands = json.dumps(Commander.commands, separators=(",", ":"))
    response = requests.post(
        "https://algorithm-visualizer.org/api/visualizations",
        headers={"Content-type": "application/json"},
        data=commands
    )

    if response.status_code == 200:
        return response.text
    else:
        raise requests.HTTPError(response=response)


@atexit.register
def execute():
    if os.getenv("ALGORITHM_VISUALIZER"):
        create_json_file()
    else:
        url = get_url()
        webbrowser.open(url)

