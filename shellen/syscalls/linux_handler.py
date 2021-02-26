import os
from os.path import join

from syscalls.base_handler import SysHandler


class LinuxSysHandler(SysHandler):
    def __init__(self):
        super().__init__()
        self.dir = join(os.path.dirname(os.path.realpath(__file__)),
                        'linux_tables')
        self.load_tables()
        self._args_order = {
            # shellen supported archs
            # arm/EABI'
            'arm32': ['R7', 'R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6'],
            'arm_tb': ['R7', 'R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6'],
            # oabi uses the swi NR instruction, so the first "arg" is encoded
            # in the instruction itself... a bit hard to encode this in shellen
            # so I think it is safe to ignore.
            # 'arm/OABI': ['-', 'r0', 'r1', 'r2', 'r3', 'r4', 'r5', 'r6'],
            'arm64': ['W8', 'X0', 'X1', 'X2', 'X3', 'X4', 'X5', '-'],
            # mips/n32,64
            'mips32': ['A0', 'A1', 'A2', 'A3', 'A4', 'A5', '-'],
            'mips64': ['A0', 'A1', 'A2', 'A3', 'A4', 'A5', '-'],
            # mips/o32 - The mips/o32 system call convention passes arguments 
            # 5 through 8 on the user stack.
            'mips32_o': ['A0', 'A1', 'A2', 'A3', '-', '-', '-'],
            'sparc32': ['G1', 'O0', 'O1', 'O2', 'O3', 'O4', 'O5', '-'],
            'sparc64': ['G1', 'O0', 'O1', 'O2', 'O3', 'O4', 'O5', '-'],
            # ppc == powerpc?
            'ppc32': ['R0', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9'],
            'ppc64': ['R0', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', '-'],
            'x86_32': ['EAX', 'EBX', 'ECX', 'EDX', 'ESI', 'EDI', 'EBP', '-'],
            'x86_64': ['RAX', 'RDI', 'RSI', 'RDX', 'R10', 'R8', 'R9', '-'],
            # x32 == 32-bit code on 64-bit processor? anyway doesn't seem relevant
            # 'x32': ['rax', 'rdi', 'rsi', 'rdx', 'r10', 'r8', 'r9', '-'],
            # systemz aka s390, s390x
            'systemz': ['R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', '-'],
            # other architectures
            'alpha': ['V0', 'A0', 'A1', 'A2', 'A3', 'A4', 'A5', '-'],
            'arc': ['R8', 'R0', 'R1', 'R2', 'R3', 'R4', 'R5', '-'],
            'blackfin': ['P0', 'R0', 'R1', 'R2', 'R3', 'R4', 'R5', '-'],
            'ia64':
            ['R15', 'OUT0', 'OUT1', 'OUT2', 'OUT3', 'OUT4', 'OUT5', '-'],
            'm68k': ['D0', 'D1', 'D2', 'D3', 'D4', 'D5', 'A0', '-'],
            'microblaze': ['R12', 'R5', 'R6', 'R7', 'R8', 'R9', 'R10', '-'],
            'nios2': ['R2', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', '-'],
            'parisc': ['R20', 'R26', 'R25', 'R24', 'R23', 'R22', 'R21', '-'],
            'riscv': ['A7', 'A0', 'A1', 'A2', 'A3', 'A4', 'A5', '-'],
            'superh': ['R3', 'R4', 'R5', 'R6', 'R7', 'R0', 'R1', 'R2'],
            'tile': ['R10', 'R00', 'R01', 'R02', 'R03', 'R04', 'R05', '-'],
            'xtensa': ['A2', 'A6', 'A3', 'A4', 'A5', 'A8', 'A9', '-']
        }
