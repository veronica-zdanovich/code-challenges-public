from typing import List, Optional


class Solution:
    def run_commands(self, commands: List[str], arguments: List[Optional[List]], cls):
        min_stack = None
        commands_output = list()
        for index in range(len(commands)):
            if commands[index] == "MinStack":
                min_stack = cls()
                commands_output.append(None)
                continue
            if commands[index] == "push":
                commands_output.append(min_stack.push(arguments[index][0]))
                continue
            if commands[index] == "pop":
                commands_output.append(min_stack.pop())
                continue
            if commands[index] == "top":
                commands_output.append(min_stack.top())
                continue
            if commands[index] == "getMin":
                commands_output.append(min_stack.getMin())
                continue
        return commands_output
