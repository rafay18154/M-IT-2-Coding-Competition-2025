def solve():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    idx = 0
    T = int(data[idx])  # Read number of test cases
    idx += 1
    result = []
    
    for _ in range(T):
        N = int(data[idx])  # Number of monsters in each party
        idx += 1
        
        beaver_light = []
        beaver_dark = []
        encounter_light = []
        encounter_dark = []
        
        # Read Busy Beaver's monsters
        for i in range(N):
            p, s = map(int, data[idx].split())
            if s == 0:
                beaver_light.append(p)
            else:
                beaver_dark.append(p)
            idx += 1
        
        # Read encountered monsters
        for i in range(N):
            q, t = map(int, data[idx].split())
            if t == 0:
                encounter_light.append(q)
            else:
                encounter_dark.append(q)
            idx += 1
        
        # Sort the monsters by power levels
        beaver_light.sort()
        beaver_dark.sort()
        encounter_light.sort()
        encounter_dark.sort()
        
        # Try to pair light monsters
        light_possible = True
        beaver_idx = 0
        for q in encounter_light:
            while beaver_idx < len(beaver_light) and not (beaver_light[beaver_idx] >= q or 2 * beaver_light[beaver_idx] >= q):
                beaver_idx += 1
            if beaver_idx == len(beaver_light):  # No monster can defeat this one
                light_possible = False
                break
            beaver_idx += 1
        
        # Try to pair dark monsters
        dark_possible = True
        beaver_idx = 0
        for q in encounter_dark:
            while beaver_idx < len(beaver_dark) and not (beaver_dark[beaver_idx] >= q or 2 * beaver_dark[beaver_idx] >= q):
                beaver_idx += 1
            if beaver_idx == len(beaver_dark):  # No monster can defeat this one
                dark_possible = False
                break
            beaver_idx += 1
        
        # If both light and dark monsters can be paired, return YES, else NO
        if light_possible and dark_possible:
            result.append("YES")
        else:
            result.append("NO")
    
    # Output all results at once to avoid repeated IO operations
    sys.stdout.write("\n".join(result) + "\n")

