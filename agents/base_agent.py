
"""
This is  the parent class for all others'
agents including the every necessary and
common functionalities.
"""

class BaseAgent:
    def __init__(self, llm,tools, memory):
        self.llm = llm
        self.tools = tools
        self.memory = memory

    def run(self, input):
        # Common run logic, e.g tool selections, memory updates
        pass
