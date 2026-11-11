import json
FILE_NAME = "task.json"
def load_tasks():
    try:
        with open(FILE_NAME, "r", encoding = "utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("format error")
        return None
    except OSError as e:
        print(f"Can't read file: {e}")
        return None

def save_tasks(tasks):
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4, ensure_ascii=False)
        return True
    except OSError as e:
        print(f"can't save: {e}")
        return False
def show_tasks(tasks):
    if not tasks:
        print("No tasks")
        return
    for i, task in enumerate(tasks, start=1):
        status = "[x]" if task["done"] else "[]"
        print(f"{i}. {status} {task['title']}")

def main():
    tasks = load_tasks()

    if tasks is None:
        print("无法加载任务，程序退出。")
        return

    while True:
        print("\n===== TODO CLI =====")
        print("1. 查看任务")
        print("2. 添加任务")
        print("3. 完成任务")
        print("4. 删除任务")
        print("5. 退出")

        choice = input("请选择操作: ")

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            title = input("输入任务名称: ").strip()

            if not title:
                print("任务名称不能为空！")
                continue

            new_tasks = tasks + [
                {"title": title, "done": False}
            ]

            if save_tasks(new_tasks):
                tasks = new_tasks
                print("添加成功！")

        elif choice == "3":
            show_tasks(tasks)

            try:
                index = int(input("输入任务编号: ")) - 1

                if 0 <= index < len(tasks):
                    new_tasks = [task.copy() for task in tasks]
                    new_tasks[index]["done"] = True

                    if save_tasks(new_tasks):
                        tasks = new_tasks
                        print("任务已完成！")
                else:
                    print("无效的任务编号！")

            except ValueError:
                print("请输入有效的数字！")

        elif choice == "4":
            show_tasks(tasks)

            try:
                index = int(input("输入要删除的编号: ")) - 1

                if 0 <= index < len(tasks):
                    new_tasks = tasks.copy()
                    new_tasks.pop(index)

                    if save_tasks(new_tasks):
                        tasks = new_tasks
                        print("删除成功！")
                else:
                    print("无效的任务编号！")

            except ValueError:
                print("请输入有效的数字！")

        elif choice == "5":
            print("再见！")
            break

        else:
            print("无效选项！")


if __name__ == "__main__":
    main()
