import unittest

from algorithm_visualizer import commander
from algorithm_visualizer import Commander
from algorithm_visualizer.types import UNDEFINED


class CommanderTests(unittest.TestCase):
    def setUp(self):
        self.commander = Commander()

    def test_commander_create(self):
        old_count = Commander._objectCount

        args = [1, 2, 3]
        cmder = Commander(*args)
        cmd = Commander.commands[-1]

        expected_cmd = {
            "key": cmder.key,
            "method": "Commander",
            "args": args,
        }

        self.assertEqual(old_count + 1, Commander._objectCount)
        self.assertEqual(cmd, expected_cmd)

    def test_commander_max_commands(self):
        old_cmds = Commander.commands
        Commander.commands = [None for _ in range(commander._MAX_COMMANDS)]

        with self.assertRaisesRegex(RuntimeError, "Too Many Commands"):
            self.commander.command("foo")

        Commander.commands = old_cmds

    def test_commander_max_objects(self):
        old_count = Commander._objectCount
        Commander._objectCount = 200

        with self.assertRaisesRegex(RuntimeError, "Too Many Objects"):
            Commander()

        Commander._objectCount = old_count

    def test_commander_command(self):
        args = [["bar", "baz"], 12]
        self.commander.command("foo", *args, UNDEFINED)
        cmd = Commander.commands[-1]

        expected_cmd = {
            "key": self.commander.key,
            "method": "foo",
            "args": args,
        }

        self.assertEqual(cmd, expected_cmd)

    def test_commander_destroy(self):
        old_count = Commander._objectCount

        self.commander.destroy()
        cmd = Commander.commands[-1]

        expected_cmd = {
            "key": self.commander.key,
            "method": "destroy",
            "args": [],
        }

        self.assertEqual(old_count - 1, Commander._objectCount)
        self.assertEqual(cmd, expected_cmd)
