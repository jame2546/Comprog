q = []
qtime = []
n = int(input())
ticket = 0

for i in range(n):
    inp = input().split()
    cmd = inp[0]

    if cmd == "reset":
        ticket = int(inp[1])
    elif cmd == "new":
        print("ticket", ticket)
        q.append([ticket, int(inp[1])])
        ticket += 1
    elif cmd == "next":
        ord = q.pop(0)
        print("call", ord[0])
    elif cmd == "order":
        print("qtime", str(ord[0]), str(int(inp[1]) - int(ord[1])))
        qtime.append(int(inp[1]) - int(ord[1]))
    elif cmd == "avg_qtime":
        print(cmd, round(sum(qtime) / len(qtime), 4))
