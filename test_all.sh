#! /bin/bash

ulimit -Sv 2000000
parallel -j-4 --eta 'python testDeepsea_episodic.py {1}' ::: 64 23 56546 232143 560934 456546 123213 675676 9042045 0595345
