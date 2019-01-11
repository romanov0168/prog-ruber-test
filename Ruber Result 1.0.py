import pandas as pd

num_of_question = int(28)
f = open('All PC.txt', 'w')
for j in range(1, 25): #Для работы нужно 25 файлов
    j = str(j)
    file = 'PC №' + j + '.txt'
    f = open(file, 'r')
    name = f.readlines()[0]
    f = open('All PC.txt', 'a')
    f.write(name)
    r_answers = 0
    percent = 0
    for i in range(0, 28):
        f = open('PC №' + j + '.txt', 'r')
        line = f.readlines()[1]
        line_slice = line[2:-3]
        score = line_slice.split("', '")
        id = score[i][:-1]
        app = score[i][-1:]
        if app == '+':
            r_answers += 1
        df = pd.read_csv('a_first3.csv', encoding='cp1251', sep='|')
        cur_df = df[df['id'] == int(id)]
        fun = cur_df[0:1]
        question_type = fun['q_type'].iloc[0]
        question = fun['question'].iloc[0]
        f = open('All PC.txt', 'a')
        print(id + app + ' ' + question)
        f.write(id + app + ' ' + question + '\n')
    percent = r_answers / num_of_question * 100
    print(str(percent)[:2] + '%\n')
    f = open('All PC.txt', 'a')
    f.write(str(percent)[:2] + '%\n\n')
