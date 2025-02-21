
numbers = [1,2,3]

nlist = [n + 1 for n in numbers]
# print(nlist)

import random

names = ["Alec", "Dino", "Checker", "Ruthy", "Ninja"]

stu_scores = {stu:random.randint(50,101) for stu in names}
# print(stu_scores)

passed_scores = {stu:score for (stu, score) in stu_scores.items() if score >= 60}


print(passed_scores)