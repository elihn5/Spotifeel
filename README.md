# Spotifeel 
### A survey project for correlating mood data and Spotify statistics.

## INFO
Hello! This Github library contains all you will need in order to repurpose the Spotifeel survey infrastructure into your own survey design. 

Spotifeel is a survey designed to help measure correlations between music listening habits and user mood, using Spotify's "audio feature" data and each user's monthly top 25 tracks. 

## HOW TO USE

In order to use this code:

1) Add your Spotify Client ID and Client Secret to the clientID.txt and clientSecret.txt files
2) Set up a redirect URI to the url of your server
3) Run server.py on a server or home computer
4) Embed links into your survey
5) Collect data!

This code automatically gathers each user's data into dated .csv files, anonymized as much as possible to minimize risks to the participant. 

It only gathers audio feature data for the user's top 25 tracks over the past month -- it does **NOT** gather participant names, song names, or account usernames.

## ROADMAP

Currently, this code is a work-in-progress. Further updates will add integration with Qualtrics, and make the redirect URI more flexible. A final version can be expected by July 25th. 