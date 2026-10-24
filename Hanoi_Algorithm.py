def hanoi_solver(n):
    rods = [list(range(n,0, -1)), [], []]
    states = [f"{rods[0]} {rods[1]} {rods[2]}"]
    def solve(k, source, target, spare):
        if k == 0:
            return
        solve(k-1, source, spare, target)
        rods[target].append(rods[source].pop())
        states.append(f"{rods[0]} {rods[1]} {rods[2]}")
        solve(k-1, spare, target, source)
    solve(n, 0, 2, 1)
    return "\n".join(states)
    
print(hanoi_solver(2))
    
