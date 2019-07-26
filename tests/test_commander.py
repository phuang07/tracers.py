import unittest

from algorithm_visualizer import commander
from algorithm_visualizer import Commander


class CommanderTests(unittest.TestCase):
    def test_commander_max_commands(self):
        Commander.commands = [None for _ in range(commander._MAX_COMMANDS)]

        with self.assertRaisesRegex(RuntimeError, "Too Many Commands"):
            Commander()

        Commander.commands = []

    def test_commander_max_objects(self):
        Commander._objectCount = 200

        with self.assertRaisesRegex(RuntimeError, "Too Many Objects"):
            Commander()

        Commander._objectCount = 0

    def test_commander_command(self):
        cmder = Commander()
        args = [["bar", "baz"], 12]
        cmder.command("foo", *args)
        cmd = Commander.commands[-1]

        expected_cmd = {
            "key": cmder.key,
            "method": "foo",
            "args": args,
        }

        self.assertEqual(cmd, expected_cmd)

    def test_commander_create(self):
        old_count = Commander._objectCount

        args = [1, 2, 3]
        Commander(*args)
        cmd = Commander.commands[-1]

        self.assertEqual(old_count + 1, Commander._objectCount)
        self.assertEqual(cmd["method"], "Commander")
        self.assertEqual(cmd["args"], args)

    def test_commander_destroy(self):
        old_count = Commander._objectCount

        cmder = Commander()
        cmder.destroy()
        cmd = Commander.commands[-1]

        self.assertEqual(old_count, Commander._objectCount)
        self.assertEqual(cmd["method"], "destroy")
