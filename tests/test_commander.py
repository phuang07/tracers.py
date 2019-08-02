from algorithm_visualizer import commander
from algorithm_visualizer import Commander
from algorithm_visualizer.types import UNDEFINED

from tests import CommanderTestCase


class CommanderTests(CommanderTestCase):
    def setUp(self):
        self.commander = Commander()

    def test_commander_create(self):
        old_count = Commander._objectCount
        args = [1, 2, 3]
        cmder = Commander(*args)

        self.assertEqual(old_count + 1, Commander._objectCount)
        self.assertCommandEqual("Commander", *args, key=cmder.key)

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
        method = "foo"
        args = [["bar", "baz"], 12]
        self.commander.command(method, *args, UNDEFINED)

        self.assertCommandEqual(method, *args, key=self.commander.key)

    def test_commander_destroy(self):
        old_count = Commander._objectCount
        self.commander.destroy()

        self.assertEqual(old_count - 1, Commander._objectCount)
        self.assertCommandEqual("destroy", key=self.commander.key)
