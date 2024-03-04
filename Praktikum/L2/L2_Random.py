# Definisikan aturan produksi
rules = [
    lambda x, y: (4, y),  # Isi penuh jerigen A
    lambda x, y: (x, 3),  # Isi penuh jerigen B
    lambda x, y: (0, y),  # Kosongkan jerigen A
    lambda x, y: (x, 0),  # Kosongkan jerigen B
    lambda x, y: (4, y - (4 - x)) if x + y >= 4 else (x + y, 0),  # Tuangkan air dari B ke A
    lambda x, y: (x - (3 - y), 3) if x + y >= 3 else (0, x + y),  # Tuangkan air dari A ke B
    lambda x, y: (x + y, 0),  # Tuangkan seluruh air B ke A
    lambda x, y: (0, x + y)   # Tuangkan seluruh air A ke B
]

def solve_jug_problem():
    # Keadaan awal
    state = (0, 0)
    goal_state = (0, 2)

    print("Langkah-langkah untuk mencapai tujuan:")
    steps = 0

    while state != goal_state:
        for i, rule in enumerate(rules, 1):
            next_state = rule(*state)
            if next_state != state:
                steps += 1
                print(f"Langkah {steps}: {state} -> {next_state}")
                state = next_state
                break

    print("Tujuan tercapai!")

# Panggil fungsi untuk menyelesaikan masalah jerigen air
solve_jug_problem()
