import psycopg2


class Executor:


    def book_room(self, room, start_time, finish_time, name,):

        con = psycopg2.connect(
            database='database',
            user='postgres',
            password='30012002',
            host='localhost',
            port=5432
        )
        cursor = con.cursor()

        cursor.execute("select count(Book_id) from Rooms Where (RoomNumber = {}) and (({} < StartTime and {} < FinishTime) or ({} > StartTime and {} > FinishTime)) group by book_id".format(room, start_time,finish_time,start_time,finish_time))
        results = cursor.fetchall()
        if results != 0:
            cursor.execute("INSERT INTO Rooms (UserName, RoomNumber, StartTime, FinishTime) VALUES ('{}', '{}', '{}', '{}')".format(name, room, start_time, finish_time))
        else:
            print("Room is not free at this time!")


    def get_available_rooms(self, start_time, finish_time):

        con = psycopg2.connect(
            database='database',
            user='postgres',
            password='30012002',
            host='localhost',
            port=5432
            )
        cursor = con.cursor()
        cursor.execute("select RoomNumber from Rooms Where (({} < StartTime and {} < FinishTime) or ({} > StartTime and {} > FinishTime))".format(start_time, finish_time, start_time, finish_time))
        results = cursor.fetchall()
        return results





