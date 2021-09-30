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
    print("1. Home Team, FTHG and FTAG of 2010 Season where Aachen is the Home Team")
    query1 = """SELECT HomeTeam,FTHG,FTAG FROM Matches WHERE Season=2010 AND HomeTeam='Aachen' ORDER BY FTHG DESC"""
    print("*" * 170 + '\n', pd.read_sql_query(query1, connection), '\n' + "*" * 170)


def part_b():
    print("2. Total number of Home Games won by each team in 2016 Season ")
    query2 = """SELECT HomeTeam,COUNT(*) AS Total FROM (SELECT HomeTeam,FTR,Season FROM Matches
                                        WHERE FTR='H' AND Season=2016) GROUP BY HomeTeam"""
    print("*" * 170 + '\n', pd.read_sql_query(query2, connection), '\n' + "*" * 170)


def part_c():
    print("3. First Ten rows from Unique_Teams Table ")
    query3 = "SELECT * FROM Unique_Teams LIMIT 10"
    print("*" * 170 + '\n', pd.read_sql_query(query3, connection), '\n' + "*" * 170)


def part_d():
    print("4. Match_Id, Unique_Team_Id and Team_Name using WHERE")
    query4a = """SELECT Match_Id,Teams_in_Matches.Unique_Team_Id,TeamName FROM Unique_Teams,Teams_in_Matches
                                        WHERE Unique_Teams.Unique_Team_Id=Teams_in_Matches.Unique_Team_Id LIMIT 50"""
    print("*" * 170 + '\n', pd.read_sql_query(query4a, connection), '\n' + "*" * 170)
    print("4. Match_Id, Unique_Team_Id and Team_Name using JOIN")
    query4b = """SELECT Match_Id,Unique_Teams.Unique_Team_Id,TeamName FROM Unique_Teams INNER JOIN Teams_in_Matches
                                        ON Teams_in_Matches.Unique_Team_ID=Unique_Teams.Unique_Team_Id LIMIT 50"""
    print("*" * 170 + '\n', pd.read_sql_query(query4b, connection), '\n' + "*" * 170)


def part_e():
    print("5. Joining Unique_teams Table and Teams Table")
    query5 = "SELECT * FROM Teams INNER JOIN Unique_Teams ON Teams.TeamName=Unique_Teams.TeamName LIMIT 10"
    print("*" * 170 + '\n', pd.read_sql_query(query5, connection), '\n' + "*" * 170)


def part_f():
    print(
        """6. Displaying Unique_Team_ID and TeamName from Unique_Teams Table and AvgAgeHome,Season And ForeignPlayersHome from Teams Table """)
    query6 = """SELECT Unique_Teams.Unique_Team_ID,Unique_Teams.TeamName,Teams.AvgAgeHome,Teams.Season,
                                        Teams.ForeignPlayersHome FROM Teams INNER JOIN Unique_Teams
                                        ON Teams.TeamName=Unique_Teams.TeamName LIMIT 5"""
    print("*" * 170 + '\n', pd.read_sql_query(query6, connection), '\n' + "*" * 170)


def part_g():
    print("7. Highest Match_ID for each team that ends in a 'y' or a 'r' along with TeamName and Unique_Team_ID")
    query7 = """SELECT Teams_in_Matches.Unique_Team_ID,Unique_Teams.TeamName,MAX(Match_Id) as Maximum_Match_Id
                                        FROM Teams_in_Matches INNER JOIN Unique_Teams
                                        ON Teams_in_Matches.Unique_Team_ID=Unique_Teams.Unique_Team_ID
                                        WHERE TeamName LIKE '%y' OR TeamName LIKE '%r' GROUP BY TeamName
                                        ORDER BY Teams_in_Matches.Unique_Team_ID"""
    print("*" * 170 + '\n', pd.read_sql_query(query7, connection), '\n' + "*" * 170)


if __name__ == "__main__":
    connection = connect_db('database.sqlite')
    while True:
        print("Main Menu \n" + "*" * 170 + '\n' +
              "1.Display Home Team, FTHG and FTAG of 2010 Season where Aachen is the Home Team\n" +
              "2.Display Total number of Home Games won by each team in 2016 Season\n" +
              "3.Display First Ten rows from Unique_Teams Table\n" +
              "4.Display Match_Id, Unique_Team_Id and Team_Name\n" +
              "5.Display Joining Unique_teams Table and Teams Table\n" +
              "6.Display Unique_Team_ID and TeamName from Unique_Teams Table and AvgAgeHome,Season And ForeignPlayersHome from Teams Table\n" +
              "7.Display Highest Match_ID for each team that ends in a 'y' or a 'r' along with TeamName and Unique_Team_ID\n"
              "8.Exit\n" + "*" * 170)
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
                part_f()
            elif choice == 7:
                part_g()
            elif choice == 8:
                print("Thank You")
                break
            else:
                print("Invalid Option!!!")
                continue
        except ValueError:
            print("Invalid Value!!!")
    connection.close()
