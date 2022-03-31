from executor import Executor


class Client:
    executor = Executor()

    def get_start_time(self):
        print("Enter start time")
        start_time = int(input())

        return start_time

    def get_finish_time(self):
        print("Enter finish time")
        finish_time = int(input())

        return finish_time


    def get_user_name(self):
        print("Enter your name")
        name = input()

        return name

    def get_desired_room(self):
        print("Enter room number")
        room = int(input())

        return room

    def process(self):
        is_time_to_exit = False

        while not is_time_to_exit:
            command = input()

            if command == "available_rooms":
                start_time = self.get_start_time()
                finish_time = self.get_finish_time()
                available_rooms = self.executor.get_available_rooms(start_time, finish_time)
                print(available_rooms)

            elif command == "book":
                room = self.get_desired_room()
                start_time = self.get_start_time()
                finish_time = self.get_finish_time()
                name = self.get_user_name()

                self.executor.book_room( room, start_time, finish_time, name,)

            elif command == "exit":
                is_time_to_exit = True

            else:
                print("Command is not found. Available commands: book|avilable_rooms|exit")
