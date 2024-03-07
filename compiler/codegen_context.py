"""
A container for the context information kept
for assembly code generation while walking
an abstract syntax tree.

The context object is passed around from node to
node during code generation. Having a context
object, rather than a set of different pieces
of information passed around, isolates in one
place several small design decisions:  How
registers are allocated, how constants and variables
are declared, when and how the code is actually
emitted to the output file.
"""

import logging

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


class Context(object):
    """The state of code generation"""

    def __init__(self):
        # A table of integer constants to be declared at
        # the end of the source program.  The table maps
        # values to names, so that we can reuse them.
        self.consts: dict[str, int] = {}

        # A table of variables to be declared at
        # the end of the source program, with the
        # symbols used for them in the assembly code.
        self.vars: dict[str, str] = {}

        # Instructions in the source code, as a list of
        # strings.
        self.assm_lines: list[str] = []

        # The available registers
        self.registers = [f"r{i}" for i in range(1, 15)]

    def get_const_symbol(self, value: int) -> str:
        """Returns the name of the label associated
        with a constant value, and remembers to
        declare it at the end of the source code.
        """
        assert isinstance(value, int)
        if value < 0:
            label = f"const_n_{abs(value)}"
        else:
            label = f"const_{value}"
        self.consts[value] = label
        return label

    def add_line(self, line: str):
        """Add a line of assembly code"""
        self.assm_lines.append(line)
        log.debug("Added line, now {self.assm_lines}")

    def get_lines(self) -> list[str]:
        """Get all the generated source code, including
        declarations of variables and constants.
        """
        code = self.assm_lines.copy()
        for constval in sorted(self.consts):
            code.append(f"{self.consts[constval]}:  DATA {constval}")
        for varval in sorted(self.vars):
            code.append(f"{self.vars[varval]}:  DATA 0")
        return code

    def get_var_symbol(self, name: str) -> str:
        """Returns the name of the label associated
        with a constant value, and remembers to
        declare it at the end of the source code.
        """
        label = f"var_{name}"
        self.vars[name] = label
        return label
