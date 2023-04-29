import random


def read_fortunes(file_path):
    with open(file_path, 'r') as file:
        fortunes = file.read().split('\n%')
        return [fortune.strip() for fortune in fortunes]


def get_random_fortune(fortunes):
    return random.choice(fortunes)


def main():
    file_choices = ['people', 'goedel', 'magic', 'love', 'humorists', 'cookie', 'linuxcookie', 'kids', 'news', 'wisdom',
                    'men-women', 'science', 'education', 'songs-poems', 'art', 'food', 'ascii-art', 'drugs',
                    'miscellaneous', 'ethnic', 'translate-me', 'platitudes', 'zippy', 'startrek', 'fortunes', 'sports',
                    'politics', 'definitions', 'literature', 'computers', 'pets', 'medicine', 'riddles', 'work', 'law']

    file_choice = random.choice(file_choices)
    fortunes = read_fortunes('datfiles/' + file_choice)

    fortune = get_random_fortune(fortunes)
    print(file_choice.upper() + ":\n" + fortune)


if __name__ == '__main__':
    main()
