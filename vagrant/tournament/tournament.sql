-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.


-- initiating database, it will throw a non-critical error if it already exists
CREATE DATABASE tournament;


-- dropping existing tables in the order of dependencies. All data will be lost
-- it must be removed from production and upgrades
DROP VIEW IF EXISTS winners;
DROP TABLE IF EXISTS matches;
DROP TABLE IF EXISTS players;


-- creating table players. Currently only full name in one string and 
-- ID as serial (primary key) are needed. more relevant info about player might 
-- be added in the future
CREATE TABLE players (id serial primary key,
						name text);


-- creating table matches, which records, which two players played and how is 
-- winner and loser. ID column is added because two players might meet each other 
-- repeatedly. time stamp is added for potential future use.
CREATE TABLE matches (id serial primary key,
						winner integer references players(id),
						loser integer references players(id),
						time timestamptz DEFAULT CURRENT_TIMESTAMP);

