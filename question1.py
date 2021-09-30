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
    print(
        "1. The Names of both Home Teams and Away Teams in each match played in 2015 and Full Time Home Goals (FTHG) = 5 ")
    query1 = 'SELECT HomeTeam, AwayTeam FROM Matches WHERE Season=2015 AND FTHG=5'
    print("*" * 120 + '\n', pd.read_sql_query(query1, connection), '\n' + "*" * 120)


def part_b():
    print("2. The Details of Matches were Arsenal is the Home Team and Full Time Result (FTR) is A (Away Win)")
    query2 = "SELECT * FROM Matches WHERE HomeTeam='Arsenal' AND FTR='A'"
    print("*" * 120 + '\n', pd.read_sql_query(query2, connection), '\n' + "*" * 120)


def part_c():
    print(
        "3. The Details of Matches from 2012 to 2015 where Away Team is Bayern Munich and Full Time Away Goals (FTAG) > 2")
    query3 = "SELECT * FROM Matches WHERE Season BETWEEN 2012 AND 2015 AND AwayTeam='Bayern Munich' AND FTAG>2"
    print("*" * 120 + '\n', pd.read_sql_query(query3, connection), '\n' + "*" * 120)


def part_d():
    print("4. The Details of Matches where Home Team name begins with 'A' and Away Team name begins with 'M' ")
    query4 = "SELECT * FROM Matches WHERE HomeTeam LIKE 'A%' AND AwayTeam LIKE 'M%'"
    print("*" * 120 + '\n', pd.read_sql_query(query4, connection), '\n' + "*" * 120)


if __name__ == "__main__":
    connection = connect_db('database.sqlite')
    while True:
        print("Main Menu \n" + "*" * 120 + '\n' +
              "1.Display the Names of both Home Teams and Away Teams in each match played in 2015 and Full Time Home Goals (FTHG) = 5\n" +
              "2.Display the Details of Matches were Arsenal is the Home Team and Full Time Result (FTR) is A (Away Win) \n" +
              "3.Display the Details of Matches from 2012 to 2015 where Away Team is Bayern Munich and Full Time Away Goals (FTAG) > 2 \n" +
              "4.Display the Details of Matches where Home Team name begins with 'A' and Away Team name begins with 'M' \n" +
              "5.Exit\n" + "*" * 120)
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
                print("Thank You")
                break
            else:
                print("Invalid Option!!!")
                continue
        except ValueError:
            print("Invalid Value!!!")
    connection.close()
