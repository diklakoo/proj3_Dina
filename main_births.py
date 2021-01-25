def parse_birth_file_to_dict(file_name):
    births_per_state = {}
    with open(file_name) as file:
        for line in file:
            if line.startswith('"year"'):
                continue
            else:
                line = line.rstrip().split(",")
                year = int(line[0])
                state = line[1]
                births = int(line[3])
                if 1986 <= year <= 2006:
                    if state in births_per_state:
                        births_per_state[state] = births_per_state[state] + births
                    else:
                        births_per_state[state] = births
    return births_per_state


def print_birth_per_state(dict):
    for key, val in dict.items():
        print(f" between the years 1986-2006 , {key} has {val:,}  births total.")
    print()

def main():
    birth_dict = parse_birth_file_to_dict('births.csv')
    print_birth_per_state(birth_dict)
    print_state_with_max_births(birth_dict)



def print_state_with_max_births(birth_dict):
    max_state = max(birth_dict, key=birth_dict.get)
    max_births = max(birth_dict.values())
    print(f"the state with the max births is {max_state} , with {max_births: ,} births total .")


if __name__ == '__main__':
    main()


