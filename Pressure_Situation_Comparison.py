#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd
from pprint import pprint
import json
from Pulling_Close_Games import close_games_df
from nfl_api_version import get_pbp_stats
from QBs_WRs_season_stats import wr_season_stats
import time
import numpy as np
from config import api_key


# In[2]:


close_clean = close_games_df[['Game ID', 'Home Team Name', 'Home Team Alias', 'Home Team Id', 
               'Away Team Name', 'Away Team Alias', 'Away Team Id', 
                'Final Score (Home)','Final Score (Away)', 'Game Diff (Final)',
                'Beg of the 4th Quarter Score (Home)', 
                'Beg of the 4th Quarter Score (Away)',
                'Game Diff (4th Quarter)',
                'Quarter 4 Points (Home)', 'Quarter 4 Points (Away)', 
                'Overtime Points (Home)', 'Overtime Points (Away)', 
               'Down Team Won?']]
close_clean


# In[3]:


close = close_clean[abs(close_clean['Game Diff (Final)'])<3]
close


# In[4]:


top_wr = pd.DataFrame({'Name': ['Davante Adams', 'Calvin Ridley', 'Adam Thielen', 'Mike Evans', 'Allen Robinson II', 
                               'Tyreek Hill', 'JuJu Smith-Schuster', 'Keenan Allen', 'D.K. Metcalf', 'Tyler Lockett',
                               'Stefon Diggs'],
                      'Player ID': ['e7d6ae25-bf15-4660-8b37-c37716551de3', '926e2674-52d6-4cec-9991-46ee85cc8cfd', 
                                    '2fa2b2da-4aa9-44b5-b27e-56876dfe2ad4', 'c48c21d9-0ae5-478c-ad34-30a660cfa9b8', 
                                   '0fd32417-8410-4a8f-8919-386c433bca43', '01d8aee3-e1c4-4988-970a-8c0c2d08bd83', 
                                   '9547fbb1-0d4f-4d9e-83b9-e2fa30463bb9', '5f424505-f29f-433c-b3f2-1a143a04a010',
                                   '754faf0f-40f7-45f0-b23b-6ce990ecaf26', 'dffa69ad-331e-4f09-ae38-40a5a4406be6',
                                   'a1c40664-b265-4083-aad2-54b4c734f2c5'],
                      'Player Team Alias': ['GB', 'ATL', 'MIN', 'TB', 'CHI', 'KC', 'PIT', 'LAC', 'SEA', 'SEA', 'BUF']})
top_and_close = pd.DataFrame({'Name':[],
                             'Player ID':[],
                             'Player Team Alias': [],
                             'Game ID':[]})
for i in range(len(top_wr['Player Team Alias'])):
    df = close[(close['Home Team Alias']==list(top_wr['Player Team Alias'])[i]) | (close['Away Team Alias']==list(top_wr['Player Team Alias'])[i])]
    if df.empty == False:
        top_and_close = top_and_close.append({'Name':list(top_wr['Name'])[i], 
                                              'Player ID':list(top_wr['Player ID'])[i], 
                                              'Player Team Alias': list(top_wr['Player Team Alias'])[i], 
                                              'Game ID':list(df['Game ID'])[0]}, ignore_index = True)


# In[5]:


top_wr


# In[6]:


top_and_close


# In[7]:


wr_season_stats.columns


# In[13]:


test = get_pbp_stats('a76ed880-ef6c-43a3-b2a2-f6eae7f072b2', '926e2674-52d6-4cec-9991-46ee85cc8cfd')


# In[14]:


test.columns


# In[30]:


test[['target','dropped', 'yards_after_catch']]


# In[32]:


targets = test['target'].sum()
targets


# In[29]:


wr_season_stats[wr_season_stats['Player ID']=='926e2674-52d6-4cec-9991-46ee85cc8cfd'][['Targets','Total Dropped Passes','Yards After Catch']]


# In[44]:


comparison_df = pd.DataFrame({'Name':[],
                       'Player ID':[],
                       'Player Team Alias':[],
                       'Targets':[],
                      'Dropped': [],
                      'Yards After Catch': [],
                      'Targets Season Avg': [],
                      'Dropped Season Avg': [],
                      'Yards After Catch Avg': []})

for row in range(len(top_and_close)):
    player_id = list(top_and_close['Player ID'])[row]
    game_id = list(top_and_close['Game ID'])[row]
    pressure_stats = get_pbp_stats(game_id, player_id)[['target','dropped', 'yards_after_catch']]
    targets = pressure_stats['target'].sum()
    dropped = pressure_stats['dropped'].sum()
    yac = pressure_stats['yards_after_catch'].sum()
    season_stats = wr_season_stats[wr_season_stats['Player ID']==player_id][['Targets','Total Dropped Passes','Yards After Catch']]
    targets_avg = (list(season_stats['Targets'])[0])/68
    dropped_avg = (list(season_stats['Total Dropped Passes'])[0])/68
    yac_avg = (list(season_stats['Yards After Catch'])[0])/68
    comparison_df = comparison_df.append({'Name':list(top_and_close['Name'])[row],
                       'Player ID':list(top_and_close['Player ID'])[row],
                       'Player Team Alias': list(top_and_close['Player Team Alias'])[row],
                       'Targets':pressure_stats['target'].sum(),
                      'Dropped': pressure_stats['dropped'].sum(),
                      'Yards After Catch': yac,
                      'Targets Season Avg': targets_avg,
                      'Dropped Season Avg': dropped_avg,
                      'Yards After Catch Avg': yac_avg}, ignore_index = True)


# In[49]:


comparison_df


# In[47]:


import matplotlib.pyplot as plt


# In[65]:


def plot_this_df(player_df):
    x_vals = [player_df['Targets'], player_df['Dropped'], player_df['Yards After Catch']]
    y_vals = [player_df['Targets Season Avg'],player_df['Dropped Season Avg'], player_df['Yards After Catch Avg']]
    annotations = ['Targets', 'Dropped', 'Yards After Catch']
    fig, ax = plt.subplots()
    ax.scatter(x_vals, y_vals)
    ax.set(title = f"4th Quarter 'Pressure' Game Stats vs Season Average Stats for {str(list(player_df['Name']))[2:-2]}",
          xlabel = "4th Quarter Stat",
          ylabel = "Season Avg per Quarter")
    for k, label in enumerate(annotations):
        plt.annotate(label, (x_vals[k]+0.01, y_vals[k]+0.05))
    ax.grid()
    plt.savefig(f"4th Quarter 'Pressure' Game Stats vs Season Average Stats for {str(list(player_df['Name']))[2:-2]}.png");

for i in range(len(comparison_df)):
    player_df = comparison_df[comparison_df['Name']==list(comparison_df['Name'])[i]]
    plot_this_df(player_df)


# In[ ]:




