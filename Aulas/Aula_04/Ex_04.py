# Exiba uma checklist de tarefas a fazer em um dia para o usuário,
# após isso, peça para ele dizer quais tarefas já foram concluidas

tasks = ['tomar banho', 'escovar os dentes', 'trabalhar', 'almoçar']
completed_lists = []
qt_tasks = len(tasks)

for task in enumerate(tasks):
    current_task = task[1]

    completed = input(f'\n A tarefa "{current_task}" já foi completada? (s|n): ')
    if completed == 's':
        completed_lists.append(current_task)

print('\n As tarefas concluídas foram: ')
print(completed_lists)