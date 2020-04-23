def tower_builder1(n_floors):
    floors = []
    for i in range(n_floors):
        n_floors -= 1
        floors.append(' ' * n_floors + '*' * (i * 2 + 1) + ' ' * n_floors)

    return floors

def tower_builder2(n_floors):
    result = []
    width = (n_floors * 2) - 1
    for x in range(1, 2 * n_floors, 2):
        stars = x * '*'
        line = stars.center(width)
        result.append(line)
    return result

def tower_builder3(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]

print(tower_builder2(3))
