import platform as pf
x = pf.system()
print(x)
print(pf.version())
print(pf.win32_is_iot())
print(dir(pf))

import pandas
print(dir(pandas))

import datetime as dt
print(dt.datetime.now())
