import linecache
import random
import re
from time import strptime, strftime

guff = re.compile(r"(?:coldfront_|)#.*_(\d*).*<")

def get_random_lines():
    file_path = 'minasonly.txt'
    line_number = random.randrange(1,231975)
    text = ''
    for i in range(-1,2):
        data = _get_line(file_path, line_number + i)
        if data:
            text += data[1]
            date = data[0]
    return date, text

def _get_line(filename, line_number):
    line = linecache.getline(filename,line_number)
    if line:
        m = re.match(guff, line)
        if m:
            return (strftime("%d %b %Y", strptime(m.group(1), "%Y%m%d")), re.sub(guff,"",line))
