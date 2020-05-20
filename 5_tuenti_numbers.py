import os
import sys


data_path = os.path.join("data", os.path.splitext(os.path.basename(sys.argv[0]))[0])

tc_filename = "submitInput"
tc_path = os.path.join(data_path, tc_filename)
tc_out_path = os.path.join(data_path, os.path.splitext(tc_filename)[0] + "_out")


def tuentify(num):
    n_tw = num // 20
    r = num % 20

    if 0 <= r <= n_tw*9:
        return str(n_tw)
    else:
        return "IMPOSSIBLE"

with open(tc_path, "r") as in_file:
    with open(tc_out_path, "w") as out_file:
        num_tc = int(in_file.readline().strip())

        for cidx in range(1, num_tc + 1):
            in_data = int(in_file.readline().strip())

            resp = tuentify(in_data)
            #resp = str(resp) if resp != 0 else "IMPOSSIBLE"

            out_file.write("Case #%d: %s\n" % (cidx, resp))


