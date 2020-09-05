import unittest
from typing import Optional, Union

from algorithm_visualizer import Commander
from algorithm_visualizer.types import Serializable, Undefined


class CommanderTestCase(unittest.TestCase):
    def assertCommandEqual(
        self,
        method: str,
        *args: Union[Serializable, Undefined],
        key: Optional[str] = None
    ):
        cmd = Commander.commands[-1]
        expected_cmd = {
            "key": key,
            "method": method,
            "args": list(args),
        }

        self.assertEqual(expected_cmd, cmd)
