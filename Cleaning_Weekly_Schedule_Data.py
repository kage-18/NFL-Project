#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
import pandas as pd
from pprint import pprint
import json
from config import api_key
import time
import numpy as np


# In[5]:


#Create an empty DataFrame to store the API data
weekly_games_df = pd.DataFrame()


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


# In[8]:


def team_ids(response):
    '''Grabs each team id for every game in the response'''
    team_ids = []
    for game in response['week']['games']:
        team_ids.append(game['home']['id'])
    return team_ids


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


# In[10]:


weekly_games_df.head()


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


# In[12]:


# test = weekly_games_df[weekly_games_df['Home Team Id']=='6680d28d-d4d2-49f6-aace-5292d3ec02c2']
# test[['Home Team Name', 'Away Team Name', 'Quarter 4 Points (Home)', 'Quarter 4 Points (Away)']]


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


# In[ ]:




