from config import api_key
import pandas as pd
import collections as cc
from collections import defaultdict
from pprint import pprint
import requests
import json
import numpy as np
import time



def get_qb_data(response):
    
    #passing stats
    player_id=[]
    names = []
    positions = []
    air_yards = []
    passing_attempts = []
    avg_pocket_time= []
    avg_pass= []
    batted_passes =[]
    blitzes =[]
    cmp_pct =[]
    completions =[]
    defended_passes =[]
    dropped_passes =[]
    gross_yards =[]
    hurries =[]
    interceptions =[]
    knockdowns =[]
    longest_pass =[]
    longest_touchdown_pass =[]
    net_yards_passing =[]
    on_target_throws =[]
    pocket_time =[]
    poor_throws =[]
    rating =[]
    redzone_attempts_pass =[] 
    sack_yards =[]
    sacks =[]
    spikes =[]
    throw_aways =[]
    touchdowns_pass =[]
    yards_passing =[]
    
    #rushing stats
    scrambles =[]
    rushing_attempts=[]
    avg_yards_rush=[]
    broken_tackles=[]
    kneel_downs=[]
    longest_rush=[]
    longest_touchdown_run=[]
    redzone_attempts_rush=[]
    tlost=[]
    tlost_yards_rushing=[]
    touchdowns_rushing=[]
    yards_rushing=[]
    yards_after_contact=[]
    
    #fumbles
    fumbles=[]
    lost_fumbles=[]
         
    
    for players in response['players']:
        
        
        try:
            player_id.append(players['id'])
        except:
            player_id.append(None)
        
        try: 
            names.append(players['name'])
        except: 
            names.append(None)
        
        try:
            positions.append(players['position'])
        except:
            positions.append(None)
         
        #passing stats
        try:
            air_yards.append(players['passing']['air_yards'])
        except:
            air_yards.append(None)
        
        try:
            passing_attempts.append(players['passing']['attempts'])
        except:
            passing_attempts.append(None)
        
        try:
            avg_pocket_time.append(players['passing']['avg_pocket_time'])
        except:
            avg_pocket_time.append(None)
        
        try:
            avg_pass.append(players['passing']['avg_yards'])
        except:
            avg_pass.append(None)
           
        try:
            batted_passes.append(players['passing']['batted_passes'])
        except:
            batted_passes.append(None)
        
        try:
            blitzes.append(players['passing']['blitzes'])
        except:
            blitzes.append(None)
            
        try:
            cmp_pct.append(players['passing']['cmp_pct'])
        except:
            cmp_pct.append(None)
            
        try:
            completions.append(players['passing']['completions'])
        except:
            completions.append(None)
                         
        try:
            defended_passes.append(players['passing']['defended_passes'])
        except:
            defended_passes.append(None)
            
        try:
            dropped_passes.append(players['passing']['dropped_passes'])
        except:
            dropped_passes.append(None)
            
        try:
            gross_yards.append(players['passing']['gross_yards'])
        except:
            gross_yards.append(None)
            
        try:
            hurries.append(players['passing']['hurries'])
        except:
            hurries.append(None)
            
        try:
            interceptions.append(players['passing']['interceptions'])
        except:
            interceptions.append(None)
            
        try:
            knockdowns.append(players['passing']['knockdowns'])
        except:
            knockdowns.append(None)
            
        
        try:
            longest_pass.append(players['passing']['longest'])
        except:
            longest_pass.append(None)
            
        try:
            longest_touchdown_pass.append(players['passing']['longest_touchdown'])
        except:
            longest_touchdown_pass.append(None)
            
        try:
            net_yards_passing.append(players['passing']['net_yards'])
        except:
            net_yards_passing.append(None)  
            
        try:
            on_target_throws.append(players['passing']['on_target_throws'])
        except:
            on_target_throws.append(None)
            
        try:
            pocket_time.append(players['passing']['pocket_time'])
        except:
            pocket_time.append(None)
            
        try:
            poor_throws.append(players['passing']['poor_throws'])
        except:
            poor_throws.append(None)   
            
        try:
            rating.append(players['passing']['rating'])
        except:
            rating.append(None)    
            
        try:
            redzone_attempts_pass.append(players['passing']['redzone_attempts'])
        except:
            redzone_attempts_pass.append(None)   
            
        try:
            sack_yards.append(players['passing']['sack_yards'])
        except:
            sack_yards.append(None)
            
        try:
            sacks.append(players['passing']['sacks'])
        except:
            sacks.append(None)   
            
        try:
            spikes.append(players['passing']['spikes'])
        except:
            spikes.append(None)
            
        try:
            throw_aways.append(players['passing']['throw_aways'])
        except:
            throw_aways.append(None)   
            
        try:
            touchdowns_pass.append(players['passing']['touchdowns'])
        except:
            touchdowns_pass.append(None) 
            
        try:
            yards_passing.append(players['passing']['yards'])
        except:
            yards_passing.append(None) 
        
        
        #rushing stats
        try:
            scrambles.append(players['rushing']['scrambles'])
        except:
            scrambles.append("0")
            
        try:
            rushing_attempts.append(players['rushing']['attempts'])
        except:
            rushing_attempts.append("0")
            
        try:
            avg_yards_rush.append(players['rushing']['avg_yards'])
        except:
            avg_yards_rush.append("0")
            
        try:
            broken_tackles.append(players['rushing']['broken_tackles'])
        except:
            broken_tackles.append("0")
            
        try:
            kneel_downs.append(players['rushing']['kneel_downs'])
        except:
            kneel_downs.append("0")
            
        try:
            longest_rush.append(players['rushing']['longest'])
        except:
            longest_rush.append("0")
            
        try:
            longest_touchdown_run.append(players['rushing']['longest_touchdown'])
        except:
            longest_touchdown_run.append("0")
            
        try:
            redzone_attempts_rush.append(players['rushing']['redzone_attempts'])
        except:
            redzone_attempts_rush.append("0")
            
        try:
            tlost.append(players['rushing']['tlost'])
        except:
            tlost.append("0")
        
        try:
            tlost_yards_rushing.append(players['rushing']['tlost_yards'])
        except:
            tlost_yards_rushing.append("0")
            
        try:
            touchdowns_rushing.append(players['rushing']['touchdowns'])
        except:
            touchdowns_rushing.append("0")
            
        try:
            yards_rushing.append(players['rushing']['yards'])
        except:
            yards_rushing.append("0")
            
        try:
            yards_after_contact.append(players['rushing']['yards_after_contact'])
        except:
            yards_after_contact.append("0")
         
        #fumbles
        try:
            fumbles.append(players['fumbles']['fumbles'])
        except:
            fumbles.append("0")
            
        try:
            lost_fumbles.append(players['fumbles']['lost_fumbles'])
        except:
            lost_fumbles.append("0")
    
    stats_df = list(zip(player_id,names, positions, air_yards, passing_attempts, avg_pocket_time, avg_pass, batted_passes,
                    cmp_pct, blitzes, completions, defended_passes, dropped_passes, gross_yards, hurries,
                    interceptions, knockdowns, longest_pass, longest_touchdown_pass, net_yards_passing,
                    on_target_throws, pocket_time, poor_throws, rating, redzone_attempts_pass, sack_yards,
                    sacks, spikes, throw_aways, touchdowns_pass, yards_passing,
                    scrambles,rushing_attempts,avg_yards_rush,broken_tackles,kneel_downs,longest_rush,
                    longest_touchdown_run,redzone_attempts_rush,tlost,tlost_yards_rushing,touchdowns_rushing,
                    yards_rushing,yards_after_contact,
                    fumbles, lost_fumbles))
               
    return stats_df




#API call
def get_all_qbs():

    team_ids=['04aa1c9d-66da-489d-b16a-1dee3f2eec4d',
    '0d855753-ea21-4953-89f9-0e20aff9eb73',
    '1f6dcffb-9823-43cd-9ff4-e7a8466749b5',
    '22052ff7-c065-42ee-bc8f-c4691c50e624',
    '2eff2a03-54d4-46ba-890e-2bc3925548f3',
    '33405046-04ee-4058-a950-d606f8c30852',
    '386bdbf9-9eea-4869-bb9a-274b0bc66e80',
    '3d08af9e-c767-4f88-a7dc-b920c6d2b4a8',
    '4254d319-1bc7-4f81-b4ab-b5e6f3402b69',
    '4809ecb0-abd3-451d-9c4a-92a90b83ca06',
    '5fee86ae-74ab-4bdd-8416-42a9dd9964f3',
    '6680d28d-d4d2-49f6-aace-5292d3ec02c2',
    '768c92aa-75ff-4a43-bcc0-f2798c2e1724',
    '7b112545-38e6-483c-a55c-96cf6ee49cb8',
    '7d4fcc64-9cb5-4d1b-8e75-8a906d1e1576',
    '82cf9565-6eb9-4f01-bdbd-5aa0d472fcd9',
    '82d2d380-3834-4938-835f-aec541e5ece7',
    '97354895-8c77-4fd4-a860-32e62ea7382a',
    'a20471b4-a8d9-40c7-95ad-90cc30e46932',
    'ad4ae08f-d808-42d5-a1e6-e9bc4e34d123',
    'c5a59daa-53a7-4de0-851f-fb12be893e9e',
    'cb2f9f1f-ac67-424e-9e72-1475cb0ed398',
    'ce92bd47-93d5-4fe9-ada4-0fc681e6caa0',
    'd26a1ca5-722d-4274-8f97-c92e49c96315',
    'd5a2eb42-8065-4174-ab79-0a6fa820e35e',
    'de760528-1dc0-416a-a978-b510d20692ff',
    'e627eec7-bbae-4fa4-8e73-8e1d6bc5c060',
    'e6aa13a4-0055-48a9-bc41-be28dc106929',
    'ebd87119-b331-4469-9ea6-d51fe3ce2f1c',
    'f0e724b0-4cbf-495a-be47-013907608da9',
    'f14bf5cc-9a82-4a38-bc15-d39f75ed5314',
    'f7ddd7fa-0bae-4f90-bc8e-669e4d6cf2de']
        
    df_season_qb = pd.DataFrame()
    base_url = 'http://api.sportradar.us/nfl/official/trial/v6/en/seasons/2019/REG/teams/'
    urls= [] 
    for i in range(len(team_ids)):
    
        url = base_url + (team_ids[i]) + '/statistics.json?api_key=' + api_key
        urls.append(url)
        
        qb = get_qb_data(requests.get(url).json())
        #print(qb)
        time.sleep(1)
         
        df_season_qb =df_season_qb.append(qb)

    #df = pd.DataFrame(df_season_stats)
    qbs = df_season_qb.dropna(how='any')
    
    return qbs
   

#Explodes multiple columns and removes list surrounding dictionary
def explode_cols(df, lst_cols, fill_value=''):
    # make sure `lst_cols` is a list
    if lst_cols and not isinstance(lst_cols, list):
        lst_cols = [lst_cols]
    # all columns except `lst_cols`
    idx_cols = df.columns.difference(lst_cols)

    # calculate lengths of lists
    lens = df[lst_cols[0]].str.len()

    if (lens > 0).all():
        # ALL lists in cells aren't empty
        return pd.DataFrame({
            col:np.repeat(df[col].values, df[lst_cols[0]].str.len())
            for col in idx_cols
        }).assign(**{col:np.concatenate(df[col].values) for col in lst_cols}) \
          .loc[:, df.columns]
    else:
        # at least one list in cells is empty
        return pd.DataFrame({
            col:np.repeat(df[col].values, df[lst_cols[0]].str.len())
            for col in idx_cols
        }).assign(**{col:np.concatenate(df[col].values) for col in lst_cols}) \
          .append(df.loc[lens==0, idx_cols]).fillna(fill_value) \
          .loc[:, df.columns]


def get_pbp_stats(game_id, player_id):
    
    All_Players_df = pd.DataFrame()

# for i in range(len(game_ids)):
    #game_id = game_ids[i]
   # print(game_id)
    #for j in range(len(player_ids)):
    play_by_play_url = f"http://api.sportradar.us/nfl/official/trial/v6/en/games/{game_id}/pbp.json?api_key={api_key}"
  #  print(play_by_play_url)
  #  print(game_id)


    game_data = requests.get(play_by_play_url).json()

    #pprint(game_data)
    #print(player_id)
   # print(play_by_play_url)
   # period=[]

#         for k in game_data["periods"]:
#             period.append(k)

#         game_data_df = pd.DataFrame(period)


    idx_list=[]

    for period in game_data["periods"][3]:
        for l in range(len(game_data["periods"][3])):
            for g in game_data["periods"][3].values():
                 if type(g) == list: # or type(j) == dict :
                    idx_list.append([l,g]) 

    # Store PBP list as Dictionary 
    dict_list = defaultdict(list)

    for p in idx_list:
        dict_list[p[0]].append(p[1])

    dict_list

    # Store Key value pairs into PBP Data Frame
    kv_df = pd.DataFrame(dict([(k, pd.Series(v)) for k,v in dict_list.items()])).T

    kv_df

    # Take in the dataframe, convert to JSON then use orient to position the data correctly.
    # json normalize will take in the dictionary rows and convert to unnested form unless
    # its values are lists of new dictionaries 
    json_struct = json.loads(kv_df.to_json(orient="records"))

    df_exp = pd.json_normalize(json_struct)

    exp_df = explode_cols(df_exp, lst_cols=list(df_exp.columns))

    exp_df

    # Breaks down first nested list and dictionary in the df
    nn=exp_df["0"].apply(pd.Series)

    json_stru = json.loads(nn.to_json(orient="records"))

    pbp_df = pd.json_normalize(json_stru)

    # Removes list around Events dictionary
    pbp_exp_df = pbp_df.explode("events")

    mm=pbp_exp_df["events"].apply(pd.Series)

    json_stru = json.loads(mm.to_json(orient="records"))

    # Events_df contains all plays in a drive 
    events_df = pd.json_normalize(json_stru)
    events_df = events_df.loc[events_df["type"] == "play"]


    # Stats as dataframe
    exp_events_df = events_df.explode("statistics")

    ss=exp_events_df["statistics"].apply(pd.Series)

    json_stru = json.loads(ss.to_json(orient="records"))

    stats_df = pd.json_normalize(json_stru)

    stats_df = stats_df.drop_duplicates(keep="first")

    #print(player_ids[j])

    # Filter data. Only bring back stats for specific player
    Player_df = stats_df.loc[stats_df["player.id"] == player_id]

    All_Players_df = All_Players_df.append(Player_df)

    time.sleep(1)

#If Player did not play then No stats will show    
    return All_Players_df