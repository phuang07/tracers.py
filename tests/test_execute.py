import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import mock

import algorithm_visualizer


class TestExecute(unittest.TestCase):
    @mock.patch.object(algorithm_visualizer.Commander, "commands", new_callable=mock.PropertyMock)
    def test_create_json_file(self, cmd_mock):
        expected_cmds = [
            {
                "key": "abc123",
                "method": "foo.bar",
                "args": [1, 2, 3],
            }
        ]
        cmd_mock.return_value = expected_cmds

        with TemporaryDirectory() as temp_dir:
            path = Path(temp_dir, "visualization.json")
            algorithm_visualizer.create_json_file(path)
            self.assertTrue(path.is_file())

            with path.open("r", encoding="UTF-8") as f:
                actual_cmds = json.load(f)

        self.assertEqual(expected_cmds, actual_cmds)

