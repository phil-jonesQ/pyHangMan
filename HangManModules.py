import random
from HangMan import *


# Word list can be improved upon and also add category feature
def rand_word_animals():
    words_animals = ['ant', 'baboon', 'badger', 'bat', 'bear', 'beaver', 'camel', 'cat', 'clam', 'cobra', 'cougar', 'coyote', 'crow', 'deer', 'dog', 'donkey', 'duck', 'eagle', 'ferret', 'fox', 'frog', 'goat', 'goose', 'hawk', 'lion', 'lizard', 'llama', 'mole', 'monkey', 'moose', 'mouse', 'mule', 'newt', 'otter', 'owl', 'panda', 'parrot', 'pigeon', 'python', 'rabbit', 'ram', 'rat', 'raven', 'rhino', 'salmon', 'seal', 'shark', 'sheep', 'skunk', 'sloth', 'snake', 'spider', 'stork', 'swan', 'tiger', 'toad', 'trout', 'turkey', 'turtle', 'weasel', 'whale', 'wolf', 'wombat', 'zebra']
    word_count = len(words_animals)
    rand_selection = random.randint(0, word_count - 1)
    print("animals " + str(rand_selection) + " " + str(word_count))
    return words_animals[rand_selection]


def rand_words_names():
    words_names = ['Adam', 'Adrian', 'Alan', 'Alasdair', 'Alastair', 'Alexander', 'Alistair', 'Allan', 'Andrew', 'Angus', 'Anthony', 'Barry', 'Benjamin', 'Brian', 'Bruce', 'Bryan', 'Callum', 'Calum', 'Cameron', 'Campbell','Charles', 'Christopher', 'Colin', 'Craig', 'Daniel', 'Darren', 'David', 'Dean', 'Derek', 'Donald', 'Douglas', 'Duncan', 'Edward', 'Eric', 'Euan', 'Ewan', 'Francis', 'Frank', 'Fraser', 'Gareth','Garry', 'Gary', 'Gavin', 'George', 'Gerald', 'Gerard', 'Gordon', 'Graeme', 'Graham', 'Grant', 'Gregor', 'Greig', 'Henry', 'Hugh', 'Iain', 'Ian', 'James', 'Jamie', 'Jason', 'John', 'Jonathan', 'Joseph', 'Justin', 'Keith', 'Kenneth', 'Kevin', 'Lee', 'Malcolm', 'Marc', 'Mark', 'Martin', 'Matthew', 'Michael', 'Murray', 'Neil', 'Nicholas', 'Norman', 'Patrick', 'Paul', 'Peter', 'Philip', 'Raymond', 'Richard', 'Robert', 'Robin', 'Roderick', 'Ronald', 'Ross', 'Roy', 'Russell', 'Ryan', 'Samuel', 'Scott', 'Sean', 'Shaun', 'Simon', 'Stephen', 'Steven', 'Stewart', 'Stuart', 'Thomas', 'Timothy', 'Wayne', 'William','Aileen', 'Alison', 'Amanda', 'Andrea', 'Angela', 'Ann', 'Anne', 'Arlene', 'Audrey', 'Barbara', 'Carol', 'Caroline', 'Carolyn', 'Catherine', 'Catriona', 'Cheryl', 'Christina', 'Christine', 'Claire', 'Clare', 'Dawn', 'Debbie', 'Deborah', 'Denise', 'Diane', 'Donna', 'Elaine', 'Elizabeth', 'Emma', 'Fiona', 'Gail', 'Gayle', 'Gillian', 'Hazel', 'Heather', 'Helen', 'Jacqueline', 'Jane', 'Janet', 'Jennifer', 'Jill', 'Jillian', 'Joanna', 'Joanne', 'Judith', 'Julie', 'Karen', 'Kathleen', 'Katrina', 'Kerry', 'Kirsteen', 'Kirsten', 'Kirsty', 'Laura', 'Lee', 'Leigh', 'Lesley', 'Linda', 'Lindsay', 'Lisa', 'Lorna', 'Lorraine', 'Louise', 'Lynn', 'Lynne', 'Lynsey', 'Mandy', 'Margaret', 'Maria', 'Marie', 'Marion', 'Mary', 'Maureen', 'Melanie', 'Mhairi', 'Michelle', 'Morag', 'Nicola', 'Pamela', 'Patricia', 'Paula', 'Pauline', 'Rachel', 'Ruth', 'Samantha', 'Sandra', 'Sarah', 'Sharon', 'Shirley', 'Shona', 'Stephanie', 'Susan', 'Suzanne', 'Tracey', 'Tracy', 'Valerie', 'Victoria']
    word_count = len(words_names)
    rand_selection = random.randint(0, word_count - 1)
    print("names " + str(rand_selection) + " " + str(word_count))
    return words_names[rand_selection]


