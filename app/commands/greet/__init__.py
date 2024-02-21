from app.commands.command import Command

class GreetCommand(Command):
    def execute(self, *args, **kwargs):
        print("Hello, World!")