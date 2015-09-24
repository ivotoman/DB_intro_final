#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament

# this file is used to provide access to your database via a library of
# functions which can add, delete or query data in your database to another 
# python program (a client program). Remember that when you define a function, 
# it does not execute, it simply means the function is defined to run a 
# specific set of instructions when called.

import psycopg2
#import bleach # I need to add bleach for HTML stripping

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")

def deleteMatches():
    """Remove all the match records from the database."""
    conn=psycopg2.connect("dbname=tournament")
    c=conn.cursor()
    c.execute('DELETE FROM matches;') 
    conn.commit()
    conn.close()


def deletePlayers():
    """Remove all the player records from the database."""
    conn=psycopg2.connect("dbname=tournament")
    c=conn.cursor()
    c.execute('DELETE FROM players;') 
    conn.commit()
    conn.close()
    

def countPlayers():
    conn=psycopg2.connect("dbname=tournament")
    c=conn.cursor()
    c.execute('SELECT count(*) FROM players;')
    count = c.fetchall()
    conn.close()
    return count[0][0]
    """Returns the number of players currently registered."""


def registerPlayer(name):
    conn=psycopg2.connect("dbname=tournament")
    c=conn.cursor()
    c.execute('INSERT INTO players (name) VALUES (%s);', (name,)) #SQL injection safe?
    conn.commit()
    conn.close()



def playerStandings():
    conn=psycopg2.connect("dbname=tournament")
    c=conn.cursor()

    # c.execute('''
    #             SELECT id, name, wc, lc 
    #             FROM winners, losers 
    #             (SELECT players.id, players.name, count(players.id) as wc 
    #                 FROM players left join matches 
    #                 ON players.id = matches.winner 
    #                 GROUP BY players.id) as winners,
    #             (SELECT players.id, players.name, count(players.id) as lc 
    #                 FROM players left join matches 
    #                 ON players.id = matches.loser 
    #                 GROUP BY players.id) as losers
    #             WHERE winners.id = losers.id
    #             GROUP BY winners.id
    #             ORDER BY wc;''')

    c.execute('''
        SELECT players.id, players.name, count(matches.winner) as wc 
        FROM players left join matches
        ON players.id = matches.winner
        GROUP BY players.id
        ORDER BY wc DESC;
        ''')

    winners = c.fetchall()

    c.execute('''
        SELECT players.id, players.name, count(matches.loser) as lc 
        FROM players left join matches
        ON players.id = matches.loser 
        GROUP BY players.id;
        ''')
    losers = c.fetchall()

    table = []
    for winner in winners:
        for loser in losers:
            if loser[0] == winner[0]:
                table.append((winner[0], winner[1], winner[2], winner[2]+loser[2]))

    conn.close()
    return table

    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """


def dbquery(dbname, qtype, query):
    conn=psycopg2.connect("dbname=%s" % dbname)
    c=conn.cursor()
    c.execute(query)
    
    values = None

    if qtype == 'insert' or qtype == "delete" or qtype == "update":
        conn.commit()
        values = True

    elif qtype == 'selectall':
        values = c.fetchall()   

    elif qtype == 'selectone':
        values = c.fetchone() 
    conn.close()    
    return values

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    
    query = "INSERT INTO matches (winner, loser) VALUES (" + str(winner) + "," + str(loser) + ");"
    dbquery("tournament", "insert", query)
    
 

 
def findMatchingPlayer(player1):
    # search for all players, who have not played with a player1 and return one with highest # of wins
    
    query = """
        SELECT w.id 
        FROM players, matches 
        WHERE (winner = %s and loser = %s) or (loser = %s and winner = %s)
        """
    matching_player = dbquery("tournament", "selectone", query)

def swissPairings():
    standings = playerStandings()
    n = 0
    pairings = []

    while n < len(standings)-1: 

        next = 1
        pairings.append((standings[n][0], standings[n][1], standings[n+next][0], standings[n+next][1]))
        n += 2

    

    return pairings

    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """


# deleteMatches()
# print 
# deletePlayers()
# print
# print "countPlayers()"
# print countPlayers()
# print
# print registerPlayer("John")
# print registerPlayer("Mary")
# print
# print "countPlayers()"
# print countPlayers()
# print 
# print "playerStandings()"
# print playerStandings()
# print reportMatch(1, 2)
print "swissPairings()"
print swissPairings()
