from termcolor import cprint, colored
from tabulate import tabulate

class Tasks:
    __title = ''
    __tasks = []
    __task_statuses = {
        "new": {"color": "blue"},
        "in progress": {"color": "yellow"},
        "completed": {"color": "green"},
        "canceled": {"color": "red"}
    }

    def set_status(self, object, status='new'):
        result = []
        if isinstance(object, list):
            for el in object:
                result.append({el: {'status': status}})
        else:
            result.append({str(object): {'status': status}})
        return result

    def __init__(self, title, task_list=[]):
        self.__title = title
        self.__add__(task_list)

    def __str__(self):
        return colored(self.__title, 'yellow')
    
    def __add__(self, new_task):
        self.__tasks += self.set_status(new_task) if isinstance(new_task, list) else [self.set_status(new_task)]
        return self

    @property
    def tasks(self):
        return self.__tasks
    
    @property
    def task_statuses(self):
        return self.__task_statuses
    

    def get_task_by_index(self, index):
        for i, tsk in enumerate(self.tasks):
            if i == index:
                return tuple(tsk.keys())[0]


    def show_task_statuses(self):
        statuses = self.__task_statuses
        for index, status in enumerate(statuses, 1):
            cprint(f"{index} {status.title()}", statuses[status]['color'])

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
                tsk = tuple(object.keys())[0]
                tsk_color = colored(f"\t {object[tsk]['status']}".title(), self.__task_statuses[object[tsk]['status']]['color'])
                print(colored(index, 'yellow'), tsk, tsk_color)


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
    
    def change_task_status():
        while True:
            try:
                new_todo_list.show_tasks()
                task_num = int(get("Enter the task number: ")) - 1
                if not 0 <= task_num < len(new_todo_list.tasks):
                    raise Exception('task')
                
                new_todo_list.show_task_statuses()
                status = int(get("Enter the status number: ")) - 1
                if not 0 <= status < len(new_todo_list.task_statuses):
                    raise Exception('status')
                
                print(new_todo_list.get_task_by_index(task_num))
                print(tuple(new_todo_list.task_statuses.keys())[status])

                res = new_todo_list.set_status(new_todo_list.get_task_by_index(task_num), tuple(new_todo_list.task_statuses.keys())[status])
                print(res)
                print(f"status of {new_todo_list.get_task_by_index[task_num]} task successfully changed to {[new_todo_list.task_statuses.keys()][status]}")
            except Exception as e:
                cprint(f'Invalid {str(e)}!', 'white', 'on_red')
            except ValueError:
                cprint(f"Invalid number!", 'white', 'on_red')
                

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
            elif user_command in (str(commands[3]).lower(), '4'):
                change_task_status()
        except Exception as e:
            cprint(f'Invalid command : {str(e)}', 'white', 'on_red')
        


COMMANDS = [
    'View Tasks',
    'Add a Task',
    'Remove a Task',
    'Set task status',
    'Exit'
]
main(COMMANDS)


