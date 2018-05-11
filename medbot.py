from fuzzywuzzy import fuzz
questions = open("ques.txt", 'r+')
answers = open("ans.txt",'r+')

predic = []
answer = []


for u in questions: 
        predic.append(u)
for n in answers:
        answer.append(n)
        
print("Hi, I am medbot, Ask me your medical queries")
def query():
	inputer = raw_input("")
	for i in predic:
		r = fuzz.ratio(inputer,i)
		pr = fuzz.partial_ratio(inputer,i)
		tsr = fuzz.token_set_ratio(inputer,i)
		if pr > 95:
			index = predic.index(i)
			print 'MedBot :' + ' '+ (answer [index])
			query()
		elif r > 80:
			index = predic.index(i)
			print 'MedBot :' + ' '+ (answer [index])
			query()
		elif tsr > 85:
			index = predic.index(i)
			print 'MedBot :' + ' '+ (answer [index])
			query()
query()

questions.close()
answers.close()
