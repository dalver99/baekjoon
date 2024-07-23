n, m = map(int, input().split())

# Use sets for more efficient lookups
nohear = set()
nosee = set()

# Read 'nohear' names
for _ in range(n):
    name = input().strip()
    nohear.add(name)

# Read 'nosee' names
for _ in range(m):
    name = input().strip()
    nosee.add(name)

# Find the intersection of the two sets
nohearnosee = sorted(nohear & nosee)

# Print the results
print(len(nohearnosee))
for name in nohearnosee:
    print(name)
