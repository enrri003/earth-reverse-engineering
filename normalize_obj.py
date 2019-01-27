import sys
import math
from pathlib import Path
from tqdm import tqdm

lat = math.radians(float(sys.argv[1]))
lon = math.radians(float(sys.argv[2]))

sin_lat = math.sin(lat)
cos_lat = math.cos(lat)
sin_lon = math.sin(lon)
cos_lon = math.cos(lon)

earth_radius = 6378137
tx = earth_radius * cos_lat * cos_lon
ty = earth_radius * cos_lat * sin_lon
tz = earth_radius * sin_lat

input_file = Path(sys.argv[3])
output_file = input_file.with_name(input_file.stem + '.2.obj')

with input_file.open() as in_, output_file.open('w') as out:
    for line in tqdm(in_):
        if line.startswith("v "):
            vertex = [float(x) for x in line.split()[1:]]
            vertex[0] -= tx
            vertex[1] -= ty
            vertex[2] -= tz

            line = "v {} {} {}\n".format(*vertex)

        out.write(line)
