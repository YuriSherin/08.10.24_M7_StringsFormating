team1_name = 'Мастера кода'
team2_name = 'Волшебники Данных'
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total

# Использование %:
print('Вас приветствует команда: %(name)s' % {'name': team1_name})
print('Вас приветствует команда: %(name)s' % {'name': team2_name})
print('В команде %(name)s участников: %(num)d !' % {'name': team1_name, 'num': team1_num})
print('В команде %(name)s участников: %(num)d !' % {'name': team2_name, 'num': team2_num})

# Использование format():
print('Команда {0} решила задач: {1} за время {2} c!'.format(team1_name, score_1, team1_time))
print('Команда {name} решила задач: {num} за время {time} c!'.format(name=team2_name, num=score_2, time=team2_time))

# Использование f-строк:
print(f'Команды решили {score_1} и {score_2} задач, что в сумму составляет {score_1 + score_2} задачи.')

if score_1 > score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'

challenge_result = f'РЕЗУЛЬТАТ БИТВЫ: {result}'
print(challenge_result)