"""Test module to learn Python"""


class Task(object):
    """Declares task object"""

    def __init__(self, name, dependencies):
        self.name = name
        self.dependencies = dependencies

class TaskScheduler(object):
    """Provides methods to schedule task operations"""
    def get_sequence(self, tasks):
        """Gets object sequence.
        tasks -- List of tasks"""
        sequence = []
        processed_list = set()
        for task in tasks:
            self.process_task_and_dependencies(task, sequence, processed_list)
        return sequence

    def process_task_and_dependencies(self, task, sequence, processed_list):
        """Processes task and its dependencies
        tasks -- List of tasks
        sequence -- Output sequence
        processed_list -- set of task names already looked at"""
        if task.name not in processed_list:
            processed_list.add(task.name)
            for dependency_task in task.dependencies:
                self.process_task_and_dependencies(dependency_task, sequence, processed_list)
            sequence.append(task)

def main():
    """Main entry point"""
    task_d = Task("D", [])
    task_a = Task("A", [task_d])
    task_b = Task("B", [task_d])
    task_c = Task("C", [task_a, task_b])
    sequence = TaskScheduler().get_sequence([task_d, task_a, task_c, task_b])
    print ", ".join(t.name for t in sequence)

main()
