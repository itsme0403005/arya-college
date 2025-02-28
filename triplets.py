pythagorean_triplets = [(a, b, c) for a in range(1, 51) for b in range(a, 51) for c in range(b, 51) if a**2 + b**2 == c**2]
for triplet in pythagorean_triplets:
    print(triplet)
