from abc import ABC, abstractmethod

class Command:
    def execute(self, *args, **kwargs):
        raise NotImplementedError("Subclasses must implement execute method")

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        if command_name in self.commands:
            self.commands[command_name].execute()
        else:
            print(f"No such command: {command_name}")

