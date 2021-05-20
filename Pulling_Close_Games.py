#!/usr/bin/env python
# coding: utf-8

# ## Pulling Close Games

# Importing dependencies and our data frame created with our game data for each game in the 2020 regular and post season

# In[1]:


import requests
import pandas as pd
from pprint import pprint
import json
from Cleaning_Weekly_Schedule_Data import weekly_games_df
import time
import numpy as np


# Let's take a look at our data frame first to confirm it was properly imported and that none of the data was corrupted

# In[2]:


#pulling in DataFrame
weekly_games_df.head()


# In[3]:


#calling columns to have a quick way to reference the column names
weekly_games_df.columns


# We want to look for games where the pressure was on. One thing we can look at is what the game score was at the beginning of the 4th quarter and what the difference in final scores was for each game. Below we'll go through and add some new columns to our original data frame containing this info.

# In[4]:


#create a new df to work with without affecting our original dataframe
close_games_df = weekly_games_df
#add a column named "Game Diff (Final)" that contains the difference in final scores
close_games_df['Game Diff (Final)'] = (weekly_games_df['Final Score (Home)'] - weekly_games_df['Final Score (Away)'])
#add a column to track the score at the beginning of the 4th quarter for the home team
close_games_df['Beg of the 4th Quarter Score (Home)'] = (weekly_games_df['Quarter 1 Points (Home)'] 
                                                         + weekly_games_df['Quarter 2 Points (Home)']
                                                         + weekly_games_df['Quarter 3 Points (Home)'])
#add a column to track the score at the beginning of the 4th quarter for the away team
close_games_df['Beg of the 4th Quarter Score (Away)'] = (weekly_games_df['Quarter 1 Points (Away)'] 
                                                         + weekly_games_df['Quarter 2 Points (Away)']
                                                         + weekly_games_df['Quarter 3 Points (Away)'])
#add a column to track the difference in scores at the beginning of the 4th quarter
close_games_df['Game Diff (4th Quarter)'] = (weekly_games_df['Beg of the 4th Quarter Score (Home)'] 
                                             - weekly_games_df['Beg of the 4th Quarter Score (Away)'])


# Let's see our new df to ensure our calculations are accurate and were appropriately added to our data frame

# In[5]:


close_games_df[['Game ID', 'Home Team Name', 'Home Team Alias', 'Home Team Id', 
               'Away Team Name', 'Away Team Alias', 'Away Team Id', 
                'Final Score (Home)','Final Score (Away)', 'Game Diff (Final)',
                'Beg of the 4th Quarter Score (Home)', 
                'Beg of the 4th Quarter Score (Away)',
                'Game Diff (4th Quarter)',
                'Quarter 4 Points (Home)', 'Quarter 4 Points (Away)', 
                'Overtime Points (Home)', 'Overtime Points (Away)']]


# In[6]:


len(close_games_df)


# Going through this data made us wonder if there are certain teams who "choke" in the 4th quarter more often than others and blow their leads in the 4th quarter. We're going to loop through and add in another column to our data frame to see if the team that was leading going into the 4th quarter was able to hang on to their victory or was beat out in the final quarter by the opposing team.

# In[38]:


#Figure out if the team that was down in the beginning of the 4th quarter won 

#empty list to store T/F booleans
down_team_won = []
#loop through each close game 
for i in range(0, len(close_games_df['Game Diff (Final)'])):
    #if the final difference is negative and the 4th quarter difference is positive it means the 
    #team that was down at the beginning of the fourth won
    if (list(close_games_df['Game Diff (4th Quarter)'])[i]) < 0 and (list(close_games_df['Game Diff (Final)'])[i])>0:
        down_team_won.append(True)
    #if the final difference is positive and the 4th quarter difference is negative it means the 
    #team that was down at the beginning of the fourth won
    elif (list(close_games_df['Game Diff (4th Quarter)'])[i]) > 0 and (list(close_games_df['Game Diff (Final)'])[i])<0:
        down_team_won.append(True)
    #otherwise the team that was up at the beginning of the fourth won
    else:
        down_team_won.append(False)

        #adding column to dataframe
close_games_df['Down Team Won?'] = down_team_won


# Calling our df once again to make sure the appropriate data was added in and our loop worked

# In[87]:


close_clean = close_games_df[['Game ID', 'Home Team Name', 'Home Team Alias', 'Home Team Id', 
               'Away Team Name', 'Away Team Alias', 'Away Team Id', 
                'Final Score (Home)','Final Score (Away)', 'Game Diff (Final)',
                'Beg of the 4th Quarter Score (Home)', 
                'Beg of the 4th Quarter Score (Away)',
                'Game Diff (4th Quarter)',
                'Quarter 4 Points (Home)', 'Quarter 4 Points (Away)', 
                'Overtime Points (Home)', 'Overtime Points (Away)', 
               'Down Team Won?']]


# Let's check to see how many instances we have where the trailing team going into the 4th quarter actually ended up taking the win 

# In[100]:


lead_blows = close_clean[close_clean['Down Team Won?']==True]
lead_blows


# Let's dive deeper into these instances and get a list of the teams that lost their lead in the 4th Quarter

# In[101]:


leads = pd.DataFrame({'Team Name': [],
             'Team Alias': []})
for row in range(len(lead_blows)):
    if list(lead_blows['Game Diff (4th Quarter)'])[row]>0:
        #home team blew the lead
        leads = leads.append({'Team Name': list(lead_blows['Home Team Name'])[row],
                             'Team Alias': list(lead_blows['Home Team Alias'])[row]}, ignore_index = True)
    elif list(lead_blows['Game Diff (4th Quarter)'])[row]<0:
        #away team blew the lead
        leads = leads.append({'Team Name': list(lead_blows['Away Team Name'])[row],
                             'Team Alias': list(lead_blows['Away Team Alias'])[row]}, ignore_index = True)        


# Printing out our new df to confirm our loop worked and cross reference with our df above that this is accurate

# In[102]:


leads


# Now we'll group by team name so we can get a count for how many times in the season teams lost their lead in the final quarter. In this same cell we'll start setting up our x and y values to plot so we can visulaize these answers

# In[131]:


graph_data = leads.groupby('Team Name').count().reset_index().sort_values('Team Alias', ascending = False)
x_vals = list(graph_data['Team Name'])
y_vals = list(graph_data['Team Alias'])
graph_data


# Importing matplotlib in order to make a bar graph

# In[132]:


import matplotlib.pyplot as plt


# Plotting and saving our visualization... Looks like the Falcons and Chargers lose their leads more often than other teams and there are 10 teams in the NFL that never lost a game they went into the 4th Quarter leading 

# In[133]:


fig, ax = plt.subplots(figsize = (18,5));
ax.bar(x_vals, y_vals, align = 'edge');
ax.set(title = 'Leads Blown in the 4th Quarter by Team', 
      xlabel = 'Team Name', 
      ylabel = 'Number of Games Lost Where Team was Ahead at the Beginning of the 4th Quarter');
plt.xticks(rotation = 45, ha = 'right');


# In[135]:


plt.savefig('Teams Who Lost After Leading into the 4th Quarter.png')

