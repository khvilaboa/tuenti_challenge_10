
import os
import sys

data_path = os.path.join("data", os.path.splitext(os.path.basename(sys.argv[0]))[0])

tc_filename = "submitInput"
tc_path = os.path.join(data_path, tc_filename)
tc_out_path = os.path.join(data_path, os.path.splitext(tc_filename)[0] + "_out")

with open(tc_path, "r") as in_file:
    with open(tc_out_path, "w") as out_file:
        num_tc = int(in_file.readline().strip())

        for cidx in range(1, num_tc + 1):
            in_data = in_file.readline().strip().split()

            resp = "-"

            if in_data[0] != in_data[1]:
                in_data = sorted(in_data)
                print(in_data)
                if in_data[0] == "P":
                    resp = "P" if in_data[1] == "R" else "S"
                else:
                    resp = "R"

            out_file.write("Case #%d: %s\n" % (cidx, resp))


