import itertools
import os
import sys

data_path = os.path.join("data", os.path.splitext(os.path.basename(sys.argv[0]))[0])

tc_filename = "testInput"
tc_path = os.path.join(data_path, tc_filename)
tc_out_path = os.path.join(data_path, os.path.splitext(tc_filename)[0] + "_out")


def find_initial(goal_num, allowed_nums, curr=[]):
    curr_sum = sum(curr)
    for n in allowed_nums:
        if curr_sum + n > goal_num:
            return None
        elif curr_sum + n == goal_num:
            return curr + [n]
        else:
            res = find_initial(goal_num, allowed_nums, curr + [n])
            if res is not None:
                return res


def limit_occ(comb, max_occ):
    i = 1
    n = comb[0]
    cont = 1
    ncomb = []
    while i < len(comb):
        if n == comb[i] and cont < max_occ:
            cont += 1
        elif n != comb[i]:
            ncomb.extend([n]*cont)
            n = comb[i]
            cont = 1
        i += 1
    ncomb.extend([n] * cont)
    return ncomb


def find_comb(curr, goal_num, ss_sum=0, ss=[]):

    for idx, n in enumerate(curr):

        if ss_sum + n > goal_num:
            return None
        elif ss_sum + n == goal_num:
            if ss_sum == 0:
                return None
            return ss + [n]
        else:
            res = find_comb(curr[:idx]+curr[idx+1:], goal_num, ss_sum+n, ss+[n])
            if res is not None:
                return res


def find_possibilities(allowed_nums, curr, found=[]):

    if len(allowed_nums) <= 1 or len(curr) <= 1:
        return 0

    cont_possibilites = 0

    for i in range(len(allowed_nums)):
        if curr[0] >= allowed_nums[i] or sum(curr) < allowed_nums[i]:
            continue
        comb = find_comb(curr, allowed_nums[i])

        if comb is not None:
            next_curr = curr.copy()
            for n in comb:
                next_curr.remove(n)
            next_curr.append(allowed_nums[i])
            next_curr = sorted(next_curr)

            if next_curr not in found:
                found.append(next_curr)
                cont_possibilites += 1 + find_possibilities(allowed_nums, next_curr, found)
        else:
            cont_possibilites += find_possibilities(allowed_nums[i+1:], curr, found)

    return cont_possibilites


with open(tc_path, "r") as in_file:
    with open(tc_out_path, "w") as out_file:
        num_tc = int(in_file.readline().strip())

        for cidx in range(1, num_tc + 1):
            in_data = map(int,in_file.readline().strip().split())
            goal_num = next(in_data)
            restr_nums = list(in_data)

            #allowed_nums = list(range(goal_num-1, 0, -1))
            allowed_nums = list(range(1, goal_num))
            for n in restr_nums:
                allowed_nums.remove(n)

            initial = find_initial(goal_num, allowed_nums)
            print(goal_num, initial, allowed_nums)

            if initial is not None:
                poss = find_possibilities(allowed_nums, initial, [initial])
                print(1+poss)
                resp = str(1 + poss)
            else:
                print(0)
                resp = "0"

            out_file.write("Case #%d: %s\n" % (cidx, resp))


