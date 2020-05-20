import socket
import sys
import itertools


movements = {(1, -2): "2u1r",
             (-1, -2): "2u1l",
             (2, -1): "1u2r",
             (-2, -1): "1u2l",
             (1, 2): "2d1r",
             (-1, 2): "2d1l",
             (2, 1): "1d2r",
             (-2, 1): "1d2l"}


def send_last_cmd(cmd):
    sock.sendall(cmd.encode())
    data = sock.recv(1000).decode()
    return data


def get_matrix_and_coords(cmd=None):

    if cmd is not None:
        sock.sendall(cmd.encode())

    data = sock.recv(1000).decode()
    m = []
    valid_lines = 0
    for line in data.split("\n"):
        line = line.strip()
        if line == "" or line.startswith("---"):
            continue
        m.append(list(line))
        valid_lines += 1
    return m


def get_opp_cmd(cmd):
    if "d" in cmd:
        cmd = cmd.replace("d", "u")
    elif "u" in cmd:
        cmd = cmd.replace("u", "d")

    if "r" in cmd:
        cmd = cmd.replace("r", "l")
    elif "l" in cmd:
        cmd = cmd.replace("l", "r")

    return cmd


def show_matrix(m):
    for l in m:
        print("".join(l))
    print()


def solve_lab(m, curr_x, curr_y, cmds=[], tried=[(0,0)], limit_rec=5):
    print("%d, (%d, %d)" % (limit_rec, curr_x, curr_y))
    show_matrix(m)
    opp_cmd = get_opp_cmd(cmds[-1]) if len(cmds) > 0 else None

    if limit_rec == 0:
        #print("Going back (max rec)...")
        #print(opp_cmd)
        m = get_matrix_and_coords(opp_cmd)
        return m, tried

    for (x_off, y_off), cmd_u in movements.items():

        if opp_cmd is not None and cmd_u == opp_cmd:
            continue

        new_x = 2 + x_off
        new_y = 2 + y_off

        if m[new_y][new_x] == "#" or m[new_y][new_x] == "K":
            continue
        elif m[new_y][new_x] == "P":
            print(cmds + [cmd_u])
            print("solved")
            print(send_last_cmd(cmd_u))
            return None, tried
        else:
            #print(cmd_u)
            move_to = (curr_x+x_off, curr_y+y_off)
            if move_to in tried:
                #print("Skipping %s... (already visited)")
                continue
            tried.append(move_to)
            m = get_matrix_and_coords(cmd_u)
            m, tried = solve_lab(m, curr_x+x_off, curr_y+y_off, cmds + [cmd_u], tried, limit_rec-1)
            if m is None:
                return None, tried

    #print("Going back (all tried, %d)..." % limit_rec)
    #print(opp_cmd)
    m = get_matrix_and_coords(opp_cmd)
    show_matrix(m)
    return m, tried

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('52.49.91.111', 2003)
sock.connect(server_address)

m = get_matrix_and_coords()

solve_lab(m, 0, 0, limit_rec=2000)

sock.close()
