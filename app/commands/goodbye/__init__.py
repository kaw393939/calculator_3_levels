from app.commands import Command


class GoodbyeCommand(Command):
    def execute(self):
        print("Goodbye")