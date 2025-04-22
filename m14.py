def process_contest_results(lines):
    max_level = -1
    winner = ""
    pakuri_species = set()

    for line in lines:
        parts = line.strip().split(',')
        trainer_name = parts[0]
        pakuri_data = parts[1:]

        for entry in pakuri_data:
            species, level_str = entry.split('-')
            level = int(level_str)
            pakuri_species.add(species)

            if level > max_level:
                max_level = level
                winner = trainer_name

    sorted_species = sorted(pakuri_species)
    return winner, sorted_species


def main():

    try:
        with open('contest.txt', 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Input file 'contest.txt' not found.")
        return

    winner, species_list = process_contest_results(lines)

    print("Winner:", winner)
    print("Pakuri species:")
    for species in species_list:
        print(species)


if __name__ == '__main__':
    main()
