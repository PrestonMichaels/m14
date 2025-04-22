def process_contest_results(input_file):
    max_level = -1
    winner = ""
    pakuri_species = set()

    with open(input_file, 'r') as file:
        for line in file:
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


    with open('winner.txt', 'w') as f:
        f.write(winner + '\n')


    with open('pakuri.txt', 'w') as f:
        for species in sorted(pakuri_species):
            f.write(species + '\n')


def main():
    input_file = 'contest.txt'
    process_contest_results(input_file)


if __name__ == '__main__':
    main()
