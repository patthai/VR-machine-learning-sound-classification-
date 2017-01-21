import pandas as pd
import re
from unipath import Path

log_report = Path('SeriesA/dB Unity report.txt')

log = log_report.read_file()

number_float_toGets = re.findall(r'nfg: (\d+)',log)
timedeltas = re.findall(r'detaT: (\d+.\d+)',log)

number_float_toGets = [int(x) for x in number_float_toGets]
timedeltas = [float(x) for x in timedeltas]

number_float_toGets = pd.DataFrame(number_float_toGets)
timedeltas = pd.DataFrame(timedeltas)

