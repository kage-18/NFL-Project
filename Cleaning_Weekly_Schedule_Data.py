#!/usr/bin/env python
# coding: utf-8

# # Cleaning Weekly Scheduled API Data

# ### Importing Dependencies

# Importing all dependencies needed to sift through the data and clean it up acording to the information we are looking for.

# In[3]:


import requests
import pandas as pd
from pprint import pprint
import json
from config import api_key
import time
import numpy as np


# First, we'll create an empty data frame that we can append to later with our desired data

# In[5]:


#Create an empty DataFrame to store the API data
weekly_games_df = pd.DataFrame()


# We'll create a loop to pull all the necessary urls for our api calls so that our data will include the 17 weeks of the regular season and 4 weeks of post season games

# In[6]:


#Create base_url to loop with to pull the season weekly schedule and postseason weekly schedule
base_url = "http://api.sportradar.us/nfl/official/trial/v6/en/games/2020/"
#Empty list to store urls for the .get() request
urls = []
#loop through each week in the season and pull that week's schedule url and append it to the list of urls
for i in range(1,18):
    url = base_url + "REG/"+ str(i) + "/schedule.json?api_key=" + api_key
    urls.append(url)
#loop through each week in the post season and pull that week's schedule url and append it to the list of urls
for i in range(1,5):
    url = base_url + "PST/"+ str(i) + "/schedule.json?api_key=" + api_key
    urls.append(url)


# Now we're going to build a function that will pull out our wanted dataa from each api call and append that data into our empty data frame. It is built with try and except statements so that the code will continue running through the api response searching for the next wanted category even if there are instances in which the api response does not contain one specific category.

# In[7]:


def grab_base_data(response):
    '''Will take a json response from Sport Radar's Weekly Schedule NFL api 
    and return the game ID, game reference, game number, game schedule, game attendance, 
    game weather, game sr_id, game home team name and alias, game away team and alias, 
    final score and scores at the end of each quarter'''
    #empty lists to temporarily pull data for the response
    ids = []
    references = []
    numbers = []
    scheduled = []
    attendances = []
    weather = []
    sr_ids = []
    home_teams = []
    home_team_alias = []
    home_team_id = []
    away_teams = []
    away_team_alias = []
    away_team_id = []
    home_final = []
    away_final = []
    home_q1 = []
    away_q1 = []
    home_q2 = []
    away_q2 = []
    home_q3 = []
    away_q3 = []
    home_q4 = []
    away_q4 = []
    home_OT = []
    away_OT = []
    #loop through each game within the week's schedule and pull the following data
    for game in response['week']['games']:
        #we place each call within a try-except statement so we can add "None" if no info is available within the API
        try:
            ids.append(game['id'])
        except:
            ids.append(None)
        try:
            references.append(game['reference'])
        except:
            references.append(None)
        try:
            numbers.append(game['number'])
        except:
            numbers.append(None)
        try:
            scheduled.append(game['scheduled'])
        except:
            scheduled.append(None)
        try:
            attendances.append(game['attendance'])
        except:
            attendances.append(None)
        try:
            weather.append(game['weather'])
        except:
            weather.append(None)
        try:
            sr_ids.append(game['sr_id'])
        except:
            sr_ids.append(None)
        try:
            home_teams.append(game['home']['name'])
        except:
            home_teams.append(None)
        try:
            home_team_alias.append(game['home']['alias'])
        except:
            home_team_alias.append(None)
        try:
            home_team_id.append(game['home']['id'])
        except:
            home_team_id.append(None)
        try:
            away_teams.append(game['away']['name'])
        except:
            away_teams.append(None)
        try:
            away_team_alias.append(game['away']['alias'])
        except:
            away_team_alias.append(None)
        try:
            away_team_id.append(game['away']['id'])
        except:
            away_team_id.append(None)
        try:
            home_final.append(game['scoring']['home_points'])
            away_final.append(game['scoring']['away_points'])
        except:
            home_final.append(None)
            away_final.append(None)
        try:
            home_q1.append(game['scoring']['periods'][0]['home_points'])
            away_q1.append(game['scoring']['periods'][0]['away_points'])
        except:
            home_q1.append(None)
            away_q1.append(None)
        try:
            home_q2.append(game['scoring']['periods'][1]['home_points'])
            away_q2.append(game['scoring']['periods'][1]['away_points'])
        except:
            home_q2.append(None)
            away_q2.append(None)
        try:
            home_q3.append(game['scoring']['periods'][2]['home_points'])
            away_q3.append(game['scoring']['periods'][2]['away_points'])
        except:
            home_q3.append(None)
            away_q3.append(None)
        try:
            home_q4.append(game['scoring']['periods'][3]['home_points'])
            away_q4.append(game['scoring']['periods'][3]['away_points'])
        except:
            home_q4.append(None)
            away_q4.append(None)
        try:
            home_OT.append(game['scoring']['periods'][4]['home_points'])
            away_OT.append(game['scoring']['periods'][4]['away_points'])
        except:
            home_OT.append(None)
            away_OT.append(None)
    rows = list(zip(ids, references, numbers, scheduled, attendances, weather, sr_ids, 
                    home_teams, home_team_alias, home_team_id, away_teams, away_team_alias, 
                    away_team_id, home_final, away_final, home_q1, away_q1, home_q2, away_q2, 
                    home_q3, away_q3, home_q4, away_q4, home_OT, away_OT))
    return rows


# We also built the function below to pull the team ids for each of the 32 teams in the NFL. This is being done so that we may pass on this list to Michael and Johnny so they can build their functions/api calls out without having to search for the team ids.

# In[8]:


def team_ids(response):
    '''Grabs each team id for every game in the response'''
    team_ids = []
    for game in response['week']['games']:
        team_ids.append(game['home']['id'])
    return team_ids


# In this loop we'll be utilizing our two functions above to loop through our urls and pull all necessary data wanted for our data frame as well as the team ids.

# In[9]:


#Setting up an empty list to store all the team ids
unique_teams = []
#Loop through all urls and grab the response
for url in urls:
    response = requests.get(url).json()
    #adding in a time.sleep statement to force the code to wait before performing another API call
    time.sleep(1)
    #grabbing needed data about the game
    base_data = grab_base_data(response)
    #grabbing all team ids for the url provided
    unique_teams.append(team_ids(response))
    #appending game data into our DataFrame
    weekly_games_df = weekly_games_df.append(base_data)


# Print out our data frame to confirm our functions went through and pulled all data correctly.

# In[10]:


weekly_games_df.head()


# Due to the way we built our functions it is necessary to go back in and rename our columns accordingly

# In[11]:


#Rename columns to be readable and descriptive
weekly_games_df.rename(columns = {0: 'Game ID',
                                  1: 'Game Reference Number',
                                  2: 'Game Number',
                                  3: 'Scheduled Time',
                                  4: 'Attendance',
                                  5: 'Weather', 
                                  6: 'Sr_ID',
                                  7: 'Home Team Name',
                                  8: 'Home Team Alias',
                                  9: 'Home Team Id',
                                  10: 'Away Team Name',
                                  11: 'Away Team Alias',
                                  12: 'Away Team Id',
                                  13: 'Final Score (Home)',
                                  14: 'Final Score (Away)',
                                  15: 'Quarter 1 Points (Home)',
                                  16: 'Quarter 1 Points (Away)',
                                  17: 'Quarter 2 Points (Home)',
                                  18: 'Quarter 2 Points (Away)',
                                  19: 'Quarter 3 Points (Home)',
                                  20: 'Quarter 3 Points (Away)',
                                  21: 'Quarter 4 Points (Home)',
                                  22: 'Quarter 4 Points (Away)',
                                  23: 'Overtime Points (Home)',
                                  24: 'Overtime Points (Away)'}, inplace=True)


# Now we'll clean up our team ids as well to remove any duplicates. In order to do this, we'll have to take the list of lists that our function returned and flatten it so that we have one continuous list that we can call a "set()" on to return our unique list of team ids.

# In[13]:


#Take our unique teams list and flatten it so we can remove duplicates
unique_teams = list(np.concatenate(unique_teams).flat)
unique_teams


# In[14]:


#checking our length of team ids
len(unique_teams)


# In[15]:


#Removing duplicates from our ids list 
unique_teams_list = set(unique_teams)
unique_teams_list


# In[16]:


#checking to make sure we have exactly 32 teams
len(unique_teams_list)


# All done! Now we have our list of unique team ids for each of the 32 NFL teams as well as a data frame containing the following for each game played in the 2020 regular season and postseason: 
# 
# Game ID, Game Reference Number, Game Number, Scheduled Time, Attendance, Weather,  Sr_ID, Home Team Name, Home Team Alias (or abbreviation), Home Team Id,  Away Team Name, Away Team Alias (or abbreviation), Away Team Id, Final Score (Home), Final Score (Away), Quarter 1 Points scored by the Home Team, Quarter 1 Points scored by the Away Team, Quarter 2 Points scored by the Home Team, Quarter 2 Points scored by the Away Team, Quarter 3 Points scored by the Home Team, Quarter 3 Points scored by the Away Team, Quarter 4 Points scored by the Home Team, Quarter 4 Points scored by the Away Team, Overtime Points scored by the Home Team, Overtime Points scored by the Away Team

# In[ ]:




