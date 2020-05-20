

import os
import sys

data_path = os.path.join("data", os.path.splitext(os.path.basename(sys.argv[0]))[0])

tc_filename = "submitInput"
tc_path = os.path.join(data_path, tc_filename)
tc_out_path = os.path.join(data_path, os.path.splitext(tc_filename)[0] + "_out")


def find_combs(goal_sum, allowed_nums):
    combs = [1] + [0] * goal_sum

    for coin in allowed_nums:
        for j in range(coin, goal_sum + 1):
            combs[j] += combs[j - coin]
    return combs[goal_sum]


with open(tc_path, "r") as in_file:
    with open(tc_out_path, "w") as out_file:
        num_tc = int(in_file.readline().strip())

        for cidx in range(1, num_tc + 1):
            in_data = map(int,in_file.readline().strip().split())
            goal_num = next(in_data)
            restr_nums = list(in_data)

            allowed_nums = list(range(1, goal_num))
            for n in restr_nums:
                if n in allowed_nums:
                    allowed_nums.remove(n)

            combs = find_combs(goal_num, allowed_nums)

            out_file.write("Case #%d: %s\n" % (cidx, str(combs)))
