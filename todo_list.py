from termcolor import cprint, colored

class Tasks:
    __title = ''
    __tasks = []

    def __init__(self, title, task_list=[]):
        self.__title = title
        self.__add__(task_list)

    def __str__(self):
        return colored(self.__title, 'yellow')
    
    def __add__(self, new_task):
        if isinstance(new_task, list):
            self.__tasks += new_task
        else:
            self.__tasks.append(new_task)
        return self

    @property
    def tasks(self):
        return self.__tasks

    def delete_task(self, index=None):
        if isinstance(index, int):
            if not 0 <= index < len(self.tasks):
                raise Exception(colored('There is no such task', 'white', 'on_red'))
            self.tasks.pop(index)
            return colored(f'Task {index + 1} was successfully deleted', 'green')
        
        self.tasks.clear()
        return colored('Tasks were successfully delete', 'green')

    def show_tasks(self):
        if len(self.tasks) <= 0:
            cprint(f"\n{self} is empty", 'red')
        else:
            print(f"\n{self} tasks:")
            for index, object in enumerate(self.tasks, 1):
                print(colored(index, 'yellow'), object)


def main(commands):
    def get(label):
        return input(label).strip()

    new_todo_list = Tasks(get('Enter name for your new ToDoList: '), ['todo_list', 'tic_tac_toe', 'rock_paper_scissor', 'quiz_game'])
    
    def add_task():
        while True:
            new_task = get("Enter a new task: ")
            if new_task != '' or len(new_task) > 0:
                return [tsk.strip() for tsk in new_task.split('~~~')]
            cprint('Invalid task!', 'white', 'on_red')
    
    def delete_task():
        if len(new_todo_list.tasks) == 0:
            return colored('There is no such task', 'red')
        
        new_todo_list.show_tasks()
        while True:
            try:
                del_task = get("Enter the task number: ")
                if 0 < int(del_task) <= len(new_todo_list.tasks):
                    return new_todo_list.delete_task(int(del_task) - 1)
                raise Exception
            except Exception:
                cprint('Invalid task!', 'white', 'on_red')
                

    while True:
        print(f"\n{new_todo_list} menu:")
        for index, cmd in enumerate(commands, 1):
            print(index, cmd)

        try:
            user_command = get("Enter your command: ").lower()

            if user_command in (str(commands[-1]).lower(), str(len(commands))):
                break

            if user_command not in [str(cmd).lower() for cmd in commands] \
                and not 0 < int(user_command) <= len(commands):
                raise Exception
            
            if user_command in (str(commands[0]).lower(), '1'):
                new_todo_list.show_tasks()
            elif user_command in (str(commands[1]).lower(), '2'):
                new_todo_list += add_task()
            elif user_command in (str(commands[2]).lower(), '3'):
                print(delete_task())
        except Exception:
            cprint('Invalid command!', 'white', 'on_red')
        


COMMANDS = [
    'View Tasks',
    'Add a Task',
    'Remove a Task',
    'Exit'
]
main(COMMANDS)


