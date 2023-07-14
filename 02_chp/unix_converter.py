import datetime
import sys

if sys.version_info[0] == 3:
    get_input = input
else:
    raise NotImplementedError(
            "Unsupported version of Python used."
    )
print(sys.version_info[0])
