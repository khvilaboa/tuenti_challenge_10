import os
import sys
from collections import defaultdict

data_path = os.path.join("data", os.path.splitext(os.path.basename(sys.argv[0]))[0])

tc_filename = "submitInput"
tc_path = os.path.join(data_path, tc_filename)
tc_out_path = os.path.join(data_path, os.path.splitext(tc_filename)[0] + "_out")

with open(tc_path, "r") as in_file:
    with open(tc_out_path, "w") as out_file:
        num_tc = int(in_file.readline().strip())

        for cidx in range(1, num_tc + 1):
            num_ppm = int(in_file.readline().strip())
            wins = defaultdict(int)

            for midx in range(1, num_ppm + 1):
                in_data = in_file.readline().strip().split()
                winner = in_data[0] if in_data[2] == "1" else in_data[1]
                wins[winner] += 1

            print(len(wins), max(wins, key=wins.get))
            resp = max(wins, key=wins.get)

            out_file.write("Case #%d: %s\n" % (cidx, resp))


