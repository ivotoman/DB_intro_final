-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.


CREATE DATABASE tournament;
	DROP VIEW IF EXISTS winners;
	DROP TABLE IF EXISTS matches;
	DROP TABLE IF EXISTS players;

	CREATE TABLE players (id serial primary key,
							name text);

	CREATE TABLE matches (id serial primary key,
							winner serial references players(id),
							loser serial references players(id),
							time timestamptz DEFAULT CURRENT_TIMESTAMP);

