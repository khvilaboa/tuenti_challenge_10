import os
import sys

data_path = os.path.join("data", os.path.splitext(os.path.basename(sys.argv[0]))[0])

tc_filename = "submitInput"
tc_path = os.path.join(data_path, tc_filename)
tc_out_path = os.path.join(data_path, os.path.splitext(tc_filename)[0] + "_out")

dvorak = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
qwerty = ' !Q#$%&q()*}w\'e[0123456789:zW]E{@ANIHDYUJGCVPMLSRXO:KF><BT?-\\=^_`anihdyujgcvpmlsrxo;kf.,bt/_|+~'
dvorak_to_qwerty = {dvorak[i]: qwerty[i] for i in range(len(dvorak))}

with open(tc_path, "r") as in_file:
    with open(tc_out_path, "w") as out_file:
        num_tc = int(in_file.readline().strip())

        for cidx in range(1, num_tc + 1):
            in_data = in_file.readline().replace("\n", "")

            resp = "".join([dvorak_to_qwerty[c] for c in in_data])

            out_file.write("Case #%d: %s\n" % (cidx, resp))


