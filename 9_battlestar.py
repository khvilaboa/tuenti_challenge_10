

msg = "514;248;980;347;145;332"
res = "3633363A33353B393038383C363236333635313A353336"
new_res = "3A3A333A333137393D39313C3C3634333431353A37363D"

msg_vals = [ord(c) for c in msg]
res_vals = [int(res[i:i+2],16) for i in range(0,len(res),2)]
new_res_vals = [int(new_res[i:i+2],16) for i in range(0,len(new_res),2)]

key_vals = []

print("Msg vals:", msg_vals)
print("Res vals:", res_vals)

for i in range(len(msg)):
    key_val = msg_vals[i] ^ res_vals[i]
    key_vals.append(key_val)

print("Key vals:", key_vals)

res_dec = [res_vals[i] ^ key_vals[i] for i in range(len(res_vals))]
print("\nOriginal decoded:", "".join(map(chr, res_dec)))

new_res_dec = [new_res_vals[i] ^ key_vals[i] for i in range(len(new_res_vals))]
print("Original decoded:", "".join(map(chr, new_res_dec)))
