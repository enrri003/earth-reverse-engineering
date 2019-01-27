import sys
import math
from pathlib import Path
from tqdm import tqdm

lat = math.radians(float(sys.argv[1]))
lon = math.radians(float(sys.argv[2]))

input_file = Path(sys.argv[3])
output_file = input_file.with_name(input_file.stem + '.2.obj')

earth_radius = 6378137
x = earth_radius * math.cos(lat) * math.cos(lon)
y = earth_radius * math.cos(lat) * math.sin(lon)
z = earth_radius * math.sin(lat)

with input_file.open() as in_, output_file.open('w') as out:
    for line in tqdm(in_):
        if line.startswith("v "):
            vertex = [float(x) for x in line.split()[1:]]
            vertex[0] -= x
            vertex[1] -= y
            vertex[2] -= z

            line = "v {} {} {}\n".format(*vertex)

        out.write(line)
