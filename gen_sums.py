from random import randint
from misc import get_next_filename

CAT = 'sums'
template = 'template/blooklet_template.csv'

outfile = get_next_filename(CAT)
MAX_NUMERATOR = 50
MIN_NUMERATOR = 11
MAX_ANSWER = MAX_NUMERATOR * 2
TTL = 5
OPERATORS = [
	['+', '+'],
	['-', '-']
]
N_OPERATORS = len(OPERATORS)
N_OPTIONS = 4

# parse lines
lines = []
with open(template, 'r') as f:
	lines = f.readlines()
lines = {i:l for i,l in enumerate(lines)}
print(lines)


def replace_question(question_n, question_text, truth, a1='', a2='', a3='', a4='', ttl=''):
	# line 7 corresponds to qn 1
	line_n = question_n + 6
	s = f'{question_n},{question_text},{a1},{a2},{a3},{a4},{ttl},{truth},,,,,,,,,,,,,,,,,,\n'
	lines[line_n] = s

def concat_questions():
	with open(outfile, 'w') as f:
		for l in list(lines.values()):
			f.write(l)

class Question():
	def __init__(self):
		self.question_text = None
		self.truth = None
		self.options = []
		self.ttl = TTL
		self.__populate()

	def __generate_options(self, truth_idx):
		truth_value = eval(self.question_text)
		options = []
		for i in range(N_OPTIONS):
			if i == truth_idx:
				options.append(truth_value)
			else:
				option = truth_value
				while option == truth_value:
					option = randint(0, MAX_ANSWER)
				options.append(option)
		self.options = options

	def __populate(self):
		n1 = randint(MIN_NUMERATOR, MAX_NUMERATOR)
		n2 = randint(MIN_NUMERATOR, n1)
		operator, operator_str = OPERATORS[randint(0, N_OPERATORS-1)] 
		self.question_text = f'{n1} {operator} {n2}'
		truth_idx = randint(0,N_OPTIONS-1)
		self.__generate_options(truth_idx)
		self.truth = truth_idx + 1 # increment 1 as py index starts from 0

	def to_dict(self):
		a1, a2, a3, a4 = self.options
		return {'question_text': self.question_text, 'truth':self.truth, 'a1': a1, 'a2': a2, 'a3': a3, 'a4': a4, 'ttl': self.ttl}


# questions = [
# 	{'question_text': '3 + 1', 'truth':1, 'a1':'4', 'a2':'5', 'a3':'6', 'a4':'7', 'ttl':30},
# 	{'question_text': '3 + 2', 'truth':1, 'a1':'4', 'a2':'5', 'a3':'6', 'a4':'7', 'ttl':30},
# 	{'question_text': '3 + 3', 'truth':1, 'a1':'4', 'a2':'5', 'a3':'6', 'a4':'7', 'ttl':30},
# 	{'question_text': '3 + 4', 'truth':1, 'a1':'4', 'a2':'5', 'a3':'6', 'a4':'7', 'ttl':30},
# ]

questions = [Question().to_dict() for i in range(50)]

for i, q in enumerate(questions):
	question_n = i + 1
	replace_question(
		question_n,
		q['question_text'],
		q['truth'],
		a1=q['a1'],
		a2=q['a2'],
		a3=q['a3'],
		a4=q['a4'],
		ttl=q['ttl']
	)

print(list(lines.values()))
concat_questions()
