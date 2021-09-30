import sqlite3
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


def connect_db(name):
    con = sqlite3.connect(name)
    return con


def part_a():
    print("1. Count of all rows in the Teams Table ")
    query1 = "SELECT COUNT(*) AS Count FROM Teams"
    print("*" * 90 + '\n', pd.read_sql_query(query1, connection), '\n' + "*" * 90)


def part_b():
    print("2. Unique Values in the Season column of Teams Table ")
    query2 = "SELECT DISTINCT(Season) FROM Teams"
    print("*" * 90 + '\n', pd.read_sql_query(query2, connection), '\n' + "*" * 90)


def part_c():
    print("3. Largest and Smallest stadium capacity included in the Teams Table ")
    query3 = "SELECT MAX(StadiumCapacity) AS MaximumStadiumCapacity,MIN(StadiumCapacity) AS MinimumStadiumCapacity FROM Teams"
    print("*" * 90 + '\n', pd.read_sql_query(query3, connection), '\n' + "*" * 90)


def part_d():
    print("4. Sum of Squad Players for all teams during the 2014 season from Teams Table ")
    query4 = "SELECT SUM(KaderHome) AS Sum FROM Teams WHERE Season=2014"
    print("*" * 90 + '\n', pd.read_sql_query(query4, connection), '\n' + "*" * 90)


def part_e():
    print("5. Number of Goals Manchester United scored During Home Games on Average ")
    query5 = "SELECT AVG(FTHG) as AverageGoals FROM Matches WHERE HomeTeam='Man United'"
    print("*" * 90 + '\n', pd.read_sql_query(query5, connection), '\n' + "*" * 90)


if __name__ == "__main__":
    connection = connect_db('database.sqlite')
    while True:
        print("Main Menu \n" + "*" * 90 + '\n' +
              "1.Display Count of all rows in the Teams Table \n" +
              "2.Display Unique Values in the Season column of Teams Table \n" +
              "3.Display Largest and Smallest stadium capacity included in the Teams Table \n" +
              "4.Display Sum of Squad Players for all teams during the 2014 season from Teams Table \n" +
              "5.Display Number of Goals Manchester United scored During Home Games on Average \n" +
              "6.Exit\n" + "*" * 90)
        try:
            choice = int(input("Enter your Choice : "))
            if choice == 1:
                part_a()
            elif choice == 2:
                part_b()
            elif choice == 3:
                part_c()
            elif choice == 4:
                part_d()
            elif choice == 5:
                part_e()
            elif choice == 6:
                print("Thank You")
                break
            else:
                print("Invalid Option!!!")
                continue
        except ValueError:
            print("Invalid Value!!!")
    connection.close()
