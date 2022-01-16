import random
Words_list = [
    {"word": "Sky", "question": "something is starting with s \'b\'"},
    {"word": "Sedney", "question": "A capital city of Australia"},
    {"word": "Popup", "question": "Alert message"},
    {"word": "FTP", "question": "standard for File Transfer Protocol"},
    {"word": "Taxes", "question": "The position of Dallas"},
    {"word": "Islam", "question": "What your religion"},
    {"word": "Team", "question": "meaning of co-workers"},
    {"word": "Koyoto", "question": "The name of Japan anime city \'C\'"},
    {"word": "Vaccine", "question": "Synonym of medicine"},
    {"word": "Dark", "question": "The opposite of \'light\'"},
    {"word": "Yemen", "question": "Arabic Country?"},
    {"word": "easy", "question": "simple think?"},
    {"word": "Frog", "question": " Animal live in the sea?"},
    {"word": "Ring", "question": "something worn by hand?"},
    {"word": "Year", "question": "12 months ?"},
    {"word": "CPU", "question": "Brain of computer is?"},
    {"word": "Camel", "question": "Which animal has hump on its back?"},
    {"word": "Jasmine", "question": "flower is white in colour?"},
    {"word": "Oval", "question": "Shape of Egg is?"},
    {"word": "Winter", "question": " In which season we wear warm clothes?"},
    {"word": "Seven", "question": "colors are there in a rainbow?"},
    {"word": "Red", "question": "primary color?"},
    {"word": "Sun", "question": "principal source of energy for earth?"},
    {"word": "Africa", "question": "continent is known as ‘Dark’ continent?"},
    {"word": "Asia", "question": "the largest continent in the world?"},
    {"word": "Friday", "question": "the last day from week?"},
    {"word": "seven", "question": "number of days in week"},
    {"word": "france", "question": "where is effil tower"},
    {"word": "sanaa", "question": "the capital of yemen"},
    {"word": "Cairo", "question": "the capital of Egypt"},
    {"word": "iraq", "question": "Baghdad is a capital of"},
    {"word": "cars", "question": "a taxi is a type of?"},
    {"word": "Egypt", "question": " where is The Nile River'"},
    {"word": "Yemen", "question": "where is Socotra Island"},
    {"word": "Amina", "question": " mother of our massenger"},
    {"word": "songs", "question": "which You listen everyday?"},
    {"word": "lion", "question": "who is the king of the jungle?"},
    {"word": "Om Klthom", "question": "The Lady of Arabic Singing?"},
    {"word": "Oval", "question": "Shape of Egg is?"},
    {"word": "Pluto", "question": " It is one of the planets of the solar system?"},
    {"word": "china", "question": "From Southeast Asian countries?"},
    {"word": "purple", "question": "it is mean I trust You?"},
    {"word": "Sun", "question": "the biggest start in our galaxy?"},
    {"word": "Roma", "question": "one of Italia country?"},
    {"word": "sponge pop", "question": "Who lives in the sea and people are loved it ?"},
    {"word": "Bahrain", "question": "A gulf country that starts with \'b\'"},
    {"word": "Brazil", "question": "A country that hosted World Cup in 2014"},
    {"word": "Cheap", "question": "Opposite of expensive"},
    {"word": "Ready", "question": "A word describing a state"},
    {"word": "Nivada", "question": "The state where Las Vegas is located"},
    {"word": "House", "question": "Where you live"},
    {"word": "Bus", "question": "A form of public transportation"},
    {"word": "Canada", "question": "A country in South America that starts with the letter \'C\'"},
    {"word": "Need", "question": "A word similar to require"},
    {"word": "Die", "question": "The opposite of \'live\'"},
]

rand_quz = []
awnser_word = []

for i in range(1,7):
    rand_quz.append(random.choice(Words_list))

for i in range(len(rand_quz)):
    awnser_word.append(Words_list[i]['word'])

word_len = list((sorted(awnser_word, key = len , reverse=True)))
x = 0
first_square = word_len[x]


if len(first_square) <7:
    for i in first_square:
        print(i,end='      ')
    found_word = list(filter(lambda y: y.lower().startswith(first_square[0]),awnser_word))
else:
    x+=1
    sec_square = awnser_word[x]
    v_1 = sec_square

found_word = list(filter(lambda y: y.lower().startswith(first_square[0]),awnser_word))







