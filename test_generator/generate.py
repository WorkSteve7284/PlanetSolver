import rand
import random
import csv

def main() -> None:

    LENGTH = 500

    header = [rand.case('Planet Name'), rand.case('x'), rand.case('y'), rand.case('type'), rand.case('resupply'), rand.case('hostile_radius')]

    planet_names = [rand.planet_name() for _ in range(LENGTH)]
    planet_x, planet_y = rand.pos(LENGTH)
    planet_type = [rand.case(random.choice(['neutral', 'hostile'])) for _ in range(LENGTH)]
    planet_resupply = [rand.case(random.choice(['', 'oxygen', 'food'])) for _ in range(LENGTH)]
    planet_radius = [random.random() * -3 for _ in range(LENGTH)]

    earth = ['Earth', str(random.random() * 50), str(random.random() * 50), 'neutral', '', str(0)]
    target = ['Target', str(random.random() * 50 + 50), str(random.random() * 50 + 50), 'neutral', '', str(0)]

    data = [header, earth, target]

    for name, x, y, _type, resupply, radius in zip(planet_names, planet_x, planet_y, planet_type, planet_resupply, planet_radius):
        data.append([name, str(x), str(y), _type, resupply, str(radius if _type.casefold() == 'hostile' else 0)])

    with open('CSV_FILE.csv', mode='w', newline='', encoding='utf-8') as file:

        line_end = random.choice(['\r\n', '\n'])

        print(f"Using line terminator {repr(line_end)}")

        writer = csv.writer(file, lineterminator=line_end)

        writer.writerows(data)


if __name__ == "__main__":
    main()
