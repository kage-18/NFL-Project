#!/usr/bin/env python
# coding: utf-8

# In[5]:


import requests
import pandas as pd
from pprint import pprint
import json
from config import api_key
import time
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
import seaborn as sns


# In[6]:


team_ids = [
    "04aa1c9d-66da-489d-b16a-1dee3f2eec4d",
    "0d855753-ea21-4953-89f9-0e20aff9eb73",
    "1f6dcffb-9823-43cd-9ff4-e7a8466749b5",
    "22052ff7-c065-42ee-bc8f-c4691c50e624",
    "2eff2a03-54d4-46ba-890e-2bc3925548f3",
    "33405046-04ee-4058-a950-d606f8c30852",
    "386bdbf9-9eea-4869-bb9a-274b0bc66e80",
    "3d08af9e-c767-4f88-a7dc-b920c6d2b4a8",
    "4254d319-1bc7-4f81-b4ab-b5e6f3402b69",
    "4809ecb0-abd3-451d-9c4a-92a90b83ca06",
    "5fee86ae-74ab-4bdd-8416-42a9dd9964f3",
    "6680d28d-d4d2-49f6-aace-5292d3ec02c2",
    "768c92aa-75ff-4a43-bcc0-f2798c2e1724",
    "7b112545-38e6-483c-a55c-96cf6ee49cb8",
    "7d4fcc64-9cb5-4d1b-8e75-8a906d1e1576",
    "82cf9565-6eb9-4f01-bdbd-5aa0d472fcd9",
    "82d2d380-3834-4938-835f-aec541e5ece7",
    "97354895-8c77-4fd4-a860-32e62ea7382a",
    "a20471b4-a8d9-40c7-95ad-90cc30e46932",
    "ad4ae08f-d808-42d5-a1e6-e9bc4e34d123",
    "c5a59daa-53a7-4de0-851f-fb12be893e9e",
    "cb2f9f1f-ac67-424e-9e72-1475cb0ed398",
    "ce92bd47-93d5-4fe9-ada4-0fc681e6caa0",
    "d26a1ca5-722d-4274-8f97-c92e49c96315",
    "d5a2eb42-8065-4174-ab79-0a6fa820e35e",
    "de760528-1dc0-416a-a978-b510d20692ff",
    "e627eec7-bbae-4fa4-8e73-8e1d6bc5c060",
    "e6aa13a4-0055-48a9-bc41-be28dc106929",
    "ebd87119-b331-4469-9ea6-d51fe3ce2f1c",
    "f0e724b0-4cbf-495a-be47-013907608da9",
    "f14bf5cc-9a82-4a38-bc15-d39f75ed5314",
    "f7ddd7fa-0bae-4f90-bc8e-669e4d6cf2de",
]


# In[7]:


# QBs


def qb_data(response):

    # passing stats
    player_id = []
    names = []
    positions = []
    air_yards = []
    passing_attempts = []
    avg_pocket_time = []
    avg_pass = []
    batted_passes = []
    blitzes = []
    cmp_pct = []
    completions = []
    defended_passes = []
    dropped_passes = []
    gross_yards = []
    hurries = []
    interceptions = []
    knockdowns = []
    longest_pass = []
    longest_touchdown_pass = []
    net_yards_passing = []
    on_target_throws = []
    pocket_time = []
    poor_throws = []
    rating = []
    redzone_attempts_pass = []
    sack_yards = []
    sacks = []
    spikes = []
    throw_aways = []
    touchdowns_pass = []
    yards_passing = []

    # rushing stats
    scrambles = []
    rushing_attempts = []
    avg_yards_rush = []
    broken_tackles = []
    kneel_downs = []
    longest_rush = []
    longest_touchdown_run = []
    redzone_attempts_rush = []
    tlost = []
    tlost_yards_rushing = []
    touchdowns_rushing = []
    yards_rushing = []
    yards_after_contact = []

    # fumbles
    fumbles = []
    lost_fumbles = []

    for players in response["players"]:

        try:
            player_id.append(players["id"])
        except:
            player_id.append(None)

        try:
            names.append(players["name"])
        except:
            names.append(None)

        try:
            positions.append(players["position"])
        except:
            positions.append(None)

        # passing stats
        try:
            air_yards.append(players["passing"]["air_yards"])
        except:
            air_yards.append(None)

        try:
            passing_attempts.append(players["passing"]["attempts"])
        except:
            passing_attempts.append(None)

        try:
            avg_pocket_time.append(players["passing"]["avg_pocket_time"])
        except:
            avg_pocket_time.append(None)

        try:
            avg_pass.append(players["passing"]["avg_yards"])
        except:
            avg_pass.append(None)

        try:
            batted_passes.append(players["passing"]["batted_passes"])
        except:
            batted_passes.append(None)

        try:
            blitzes.append(players["passing"]["blitzes"])
        except:
            blitzes.append(None)

        try:
            cmp_pct.append(players["passing"]["cmp_pct"])
        except:
            cmp_pct.append(None)

        try:
            completions.append(players["passing"]["completions"])
        except:
            completions.append(None)

        try:
            defended_passes.append(players["passing"]["defended_passes"])
        except:
            defended_passes.append(None)

        try:
            dropped_passes.append(players["passing"]["dropped_passes"])
        except:
            dropped_passes.append(None)

        try:
            gross_yards.append(players["passing"]["gross_yards"])
        except:
            gross_yards.append(None)

        try:
            hurries.append(players["passing"]["hurries"])
        except:
            hurries.append(None)

        try:
            interceptions.append(players["passing"]["interceptions"])
        except:
            interceptions.append(None)

        try:
            knockdowns.append(players["passing"]["knockdowns"])
        except:
            knockdowns.append(None)

        try:
            longest_pass.append(players["passing"]["longest"])
        except:
            longest_pass.append(None)

        try:
            longest_touchdown_pass.append(players["passing"]["longest_touchdown"])
        except:
            longest_touchdown_pass.append(None)

        try:
            net_yards_passing.append(players["passing"]["net_yards"])
        except:
            net_yards_passing.append(None)

        try:
            on_target_throws.append(players["passing"]["on_target_throws"])
        except:
            on_target_throws.append(None)

        try:
            pocket_time.append(players["passing"]["pocket_time"])
        except:
            pocket_time.append(None)

        try:
            poor_throws.append(players["passing"]["poor_throws"])
        except:
            poor_throws.append(None)

        try:
            rating.append(players["passing"]["rating"])
        except:
            rating.append(None)

        try:
            redzone_attempts_pass.append(players["passing"]["redzone_attempts"])
        except:
            redzone_attempts_pass.append(None)

        try:
            sack_yards.append(players["passing"]["sack_yards"])
        except:
            sack_yards.append(None)

        try:
            sacks.append(players["passing"]["sacks"])
        except:
            sacks.append(None)

        try:
            spikes.append(players["passing"]["spikes"])
        except:
            spikes.append(None)

        try:
            throw_aways.append(players["passing"]["throw_aways"])
        except:
            throw_aways.append(None)

        try:
            touchdowns_pass.append(players["passing"]["touchdowns"])
        except:
            touchdowns_pass.append(None)

        try:
            yards_passing.append(players["passing"]["yards"])
        except:
            yards_passing.append(None)

        # rushing stats
        try:
            scrambles.append(players["rushing"]["scrambles"])
        except:
            scrambles.append("0")

        try:
            rushing_attempts.append(players["rushing"]["attempts"])
        except:
            rushing_attempts.append("0")

        try:
            avg_yards_rush.append(players["rushing"]["avg_yards"])
        except:
            avg_yards_rush.append("0")

        try:
            broken_tackles.append(players["rushing"]["broken_tackles"])
        except:
            broken_tackles.append("0")

        try:
            kneel_downs.append(players["rushing"]["kneel_downs"])
        except:
            kneel_downs.append("0")

        try:
            longest_rush.append(players["rushing"]["longest"])
        except:
            longest_rush.append("0")

        try:
            longest_touchdown_run.append(players["rushing"]["longest_touchdown"])
        except:
            longest_touchdown_run.append("0")

        try:
            redzone_attempts_rush.append(players["rushing"]["redzone_attempts"])
        except:
            redzone_attempts_rush.append("0")

        try:
            tlost.append(players["rushing"]["tlost"])
        except:
            tlost.append("0")

        try:
            tlost_yards_rushing.append(players["rushing"]["tlost_yards"])
        except:
            tlost_yards_rushing.append("0")

        try:
            touchdowns_rushing.append(players["rushing"]["touchdowns"])
        except:
            touchdowns_rushing.append("0")

        try:
            yards_rushing.append(players["rushing"]["yards"])
        except:
            yards_rushing.append("0")

        try:
            yards_after_contact.append(players["rushing"]["yards_after_contact"])
        except:
            yards_after_contact.append("0")

        # fumbles
        try:
            fumbles.append(players["fumbles"]["fumbles"])
        except:
            fumbles.append("0")

        try:
            lost_fumbles.append(players["fumbles"]["lost_fumbles"])
        except:
            lost_fumbles.append("0")

    rows = list(
        zip(
            player_id,
            names,
            positions,
            air_yards,
            passing_attempts,
            avg_pocket_time,
            avg_pass,
            batted_passes,
            cmp_pct,
            blitzes,
            completions,
            defended_passes,
            dropped_passes,
            gross_yards,
            hurries,
            interceptions,
            knockdowns,
            longest_pass,
            longest_touchdown_pass,
            net_yards_passing,
            on_target_throws,
            pocket_time,
            poor_throws,
            rating,
            redzone_attempts_pass,
            sack_yards,
            sacks,
            spikes,
            throw_aways,
            touchdowns_pass,
            yards_passing,
            scrambles,
            rushing_attempts,
            avg_yards_rush,
            broken_tackles,
            kneel_downs,
            longest_rush,
            longest_touchdown_run,
            redzone_attempts_rush,
            tlost,
            tlost_yards_rushing,
            touchdowns_rushing,
            yards_rushing,
            yards_after_contact,
            fumbles,
            lost_fumbles,
        )
    )

    return rows

    [
        player_id,
        names,
        positions,
        air_yards,
        passing_attempts,
        avg_pocket_time,
        avg_pass,
        batted_passes,
        cmp_pct,
        blitzes,
        completions,
        defended_passes,
        dropped_passes,
        gross_yards,
        hurries,
        interceptions,
        knockdowns,
        longest_pass,
        longest_touchdown_pass,
        net_yards_passing,
        on_target_throws,
        pocket_time,
        poor_throws,
        rating,
        redzone_attempts_pass,
        sack_yards,
        sacks,
        spikes,
        throw_aways,
        touchdowns_pass,
        yards_passing,
        scrambles,
        rushing_attempts,
        avg_yards_rush,
        broken_tackles,
        kneel_downs,
        longest_rush,
        longest_touchdown_run,
        redzone_attempts_rush,
        tlost,
        tlost_yards_rushing,
        touchdowns_rushing,
        yards_rushing,
        yards_after_contact,
        fumbles,
        lost_fumbles,
    ]


# In[8]:


def allqbs(team_ids):

    df_season_qb = pd.DataFrame()
    base_url = (
        "http://api.sportradar.us/nfl/official/trial/v6/en/seasons/2020/REG/teams/"
    )
    urls = []
    for i in range(len(team_ids)):

        url = base_url + (team_ids[i]) + "/statistics.json?api_key=" + api_key
        urls.append(url)

        qb = qb_data(requests.get(url).json())

        time.sleep(1)

        df_season_qb = df_season_qb.append(qb)

    qbs = df_season_qb.dropna(how="any")

    return qbs


# In[11]:


qb_season_stats = allqbs(team_ids)
qb_season_stats = qb_season_stats.loc[qb_season_stats[2] == "QB"]
qb_season_stats.rename(
    columns={
        0: "Player ID",
        1: "Name",
        2: "Position",
        # passing
        3: "Air Yards",
        4: "Passing Attempts",
        5: "Avg Pocket Time",
        6: "Yards Per Pass",
        7: "Batted Passes",
        8: "Completion Percent",
        9: "Times Blitzed",
        10: "Completions",
        11: "Passes Defended",
        12: "Dropped Passes",
        13: "Gross Yards",
        14: "Hurries",
        15: "Interceptions",
        16: "Knockdowns",
        17: "Longest Completion",
        18: "Longest Touchdown Pass",
        19: "Net Yards Passing",
        20: "On Target Throws",
        21: "Total Seconds in Pocket",
        22: "Poor Throws",
        23: "Rating",
        24: "Redzone Attempts Passing",
        25: "Sacked Yards",
        26: "Times Sacked",
        27: "Spikes",
        28: "Throw Aways",
        29: "Passing Touchdowns",
        30: "Yards",
        # rushing
        31: "Scrambles",
        32: "Rushing Attempts",
        33: "Yards Per Rush",
        34: "Broken Tackles",
        35: "Kneel Downs",
        36: "Longest Rush",
        37: "Longest TD Run",
        38: "Redzone Rushing Attempts",
        39: "Negative Rushes",
        40: "Yards Lost Rushing",
        41: "Rushing Touchdowns",
        42: "Total Rushing Yards",
        43: "Yards After Contact",
        # fumbles
        44: "Fumbles",
        45: "Fumbles Lost",
    },
    inplace=True,
)

qb_season_stats


# # Top blitzed QBs

# In[15]:


qb_rush = qb_season_stats[
    [
        "Name",
        "Times Blitzed",
        "Avg Pocket Time",
        "Hurries",
        "Passing Attempts",
        "Poor Throws",
        "Completions",
        "Completion Percent",
    ]
]

qb_rush = qb_rush.sort_values("Times Blitzed", ascending=False)
qb_rush = qb_rush[(qb_rush["Times Blitzed"] > 150)]

qb_rush


# In[16]:


qb_qualify = qb_season_stats[(qb_season_stats["Passing Attempts"] > 50)]


# In[19]:


x = qb_qualify["Avg Pocket Time"]
y = qb_qualify["Times Sacked"]

plt.figure(figsize=(12, 8))
plt.scatter(x, y, c=qb_qualify["Times Sacked"], cmap="cool", edgecolor="k")
plt.xlabel("Avg Seconds in Pocket", fontsize=14)
plt.ylabel("Times Sacked", fontsize=14)
plt.title("QB Pocket Time vs Sacks (min. 50 Pass Attempts)", fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.style.use("seaborn")
# plt.xlim(2,3.2)

z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x, p(x), "r--")


# In[20]:


###### WRs #######


# In[21]:


def receiver_data(response):
    player_id = []
    names = []
    # wr stats
    positions = []
    air_yards = []
    avg_yards = []
    broken_tackles = []
    catchable_passes = []
    dropped_passes = []
    longest = []
    longest_touchdown = []
    receptions = []
    redzone_targets = []
    targets = []
    touchdowns = []
    yards = []
    yards_after_catch = []
    yards_after_contact = []

    # rushing stats
    scrambles = []
    rushing_attempts = []
    avg_yards_rush = []
    broken_tackles_rush = []
    kneel_downs = []
    longest_rush = []
    longest_touchdown_run = []
    redzone_attempts_rush = []
    tlost = []
    tlost_yards_rushing = []
    touchdowns_rushing = []
    yards_rushing = []
    yards_after_contact_rush = []

    # fumbles
    fumbles = []
    lost_fumbles = []

    for players in response["players"]:

        try:
            player_id.append(players["id"])
        except:
            player_id.append(None)

        try:
            names.append(players["name"])
        except:
            names.append(None)

        try:
            positions.append(players["position"])
        except:
            positions.append(None)

        try:
            air_yards.append(players["receiving"]["air_yards"])
        except:
            air_yards.append(None)

        ####
        try:
            avg_yards.append(players["receiving"]["avg_yards"])
        except:
            avg_yards.append(None)

        try:
            broken_tackles.append(players["receiving"]["broken_tackles"])
        except:
            broken_tackles.append(None)

        try:
            catchable_passes.append(players["receiving"]["catchable_passes"])
        except:
            catchable_passes.append(None)

        try:
            dropped_passes.append(players["receiving"]["dropped_passes"])
        except:
            dropped_passes.append(None)

        try:
            longest.append(players["receiving"]["longest"])
        except:
            longest.append(None)

        try:
            longest_touchdown.append(players["receiving"]["longest_touchdown"])
        except:
            longest_touchdown.append(None)

        try:
            receptions.append(players["receiving"]["receptions"])
        except:
            receptions.append(None)

        try:
            redzone_targets.append(players["receiving"]["redzone_targets"])
        except:
            redzone_targets.append(None)

        try:
            targets.append(players["receiving"]["targets"])
        except:
            targets.append(None)

        try:
            touchdowns.append(players["receiving"]["touchdowns"])
        except:
            touchdowns.append(None)

        try:
            yards.append(players["receiving"]["yards"])
        except:
            yards.append(None)

        try:
            yards_after_catch.append(players["receiving"]["yards_after_catch"])
        except:
            yards_after_catch.append(None)

        try:
            yards_after_contact.append(players["receiving"]["yards_after_contact"])
        except:
            yards_after_contact.append(None)

        # rushing
        try:
            scrambles.append(players["rushing"]["scrambles"])
        except:
            scrambles.append("0")

        try:
            rushing_attempts.append(players["rushing"]["attempts"])
        except:
            rushing_attempts.append("0")

        try:
            avg_yards_rush.append(players["rushing"]["avg_yards"])
        except:
            avg_yards_rush.append("0")

        try:
            broken_tackles_rush.append(players["rushing"]["broken_tackles"])
        except:
            broken_tackles_rush.append("0")

        try:
            kneel_downs.append(players["rushing"]["kneel_downs"])
        except:
            kneel_downs.append("0")

        try:
            longest_rush.append(players["rushing"]["longest"])
        except:
            longest_rush.append("0")

        try:
            longest_touchdown_run.append(players["rushing"]["longest_touchdown"])
        except:
            longest_touchdown_run.append("0")

        try:
            redzone_attempts_rush.append(players["rushing"]["redzone_attempts"])
        except:
            redzone_attempts_rush.append("0")

        try:
            tlost.append(players["rushing"]["tlost"])
        except:
            tlost.append("0")

        try:
            tlost_yards_rushing.append(players["rushing"]["tlost_yards"])
        except:
            tlost_yards_rushing.append("0")

        try:
            touchdowns_rushing.append(players["rushing"]["touchdowns"])
        except:
            touchdowns_rushing.append("0")

        try:
            yards_rushing.append(players["rushing"]["yards"])
        except:
            yards_rushing.append("0")

        try:
            yards_after_contact_rush.append(players["rushing"]["yards_after_contact"])
        except:
            yards_after_contact_rush.append("0")

        try:
            fumbles.append(players["fumbles"]["fumbles"])
        except:
            fumbles.append("0")

        try:
            lost_fumbles.append(players["fumbles"]["lost_fumbles"])
        except:
            lost_fumbles.append("0")

    rows = list(
        zip(
            player_id,
            names,
            positions,
            air_yards,
            avg_yards,
            broken_tackles,
            catchable_passes,
            dropped_passes,
            longest,
            longest_touchdown,
            receptions,
            redzone_targets,
            targets,
            touchdowns,
            yards,
            yards_after_catch,
            yards_after_contact,
            scrambles,
            rushing_attempts,
            avg_yards_rush,
            broken_tackles_rush,
            kneel_downs,
            longest_rush,
            longest_touchdown_run,
            redzone_attempts_rush,
            tlost,
            tlost_yards_rushing,
            touchdowns_rushing,
            yards_rushing,
            yards_after_contact_rush,
            fumbles,
            lost_fumbles,
        )
    )

    return rows

    [
        player_id,
        names,
        positions,
        air_yards,
        avg_yards,
        broken_tackles,
        catchable_passes,
        dropped_passes,
        longest,
        longest_touchdown,
        receptions,
        redzone_targets,
        targets,
        touchdowns,
        yards,
        yards_after_catch,
        yards_after_contact,
        scrambles,
        rushing_attempts,
        avg_yards_rush,
        broken_tackles_rush,
        kneel_downs,
        longest_rush,
        longest_touchdown_run,
        redzone_attempts_rush,
        tlost,
        tlost_yards_rushing,
        touchdowns_rushing,
        yards_rushing,
        yards_after_contact_rush,
        fumbles,
        lost_fumbles,
    ]


# In[22]:


def allwrs(team_ids):

    df_season_wr = pd.DataFrame()
    base_url = (
        "http://api.sportradar.us/nfl/official/trial/v6/en/seasons/2020/REG/teams/"
    )
    urls = []
    for i in range(len(team_ids)):

        url = base_url + (team_ids[i]) + "/statistics.json?api_key=" + api_key
        urls.append(url)

        wr = receiver_data(requests.get(url).json())
        # print(qb)
        time.sleep(1)

        df_season_wr = df_season_wr.append(wr)

    # df = pd.DataFrame(df_season_stats)

    wrs = df_season_wr.dropna()

    return wrs


# In[23]:


wr_season_stats = allwrs(team_ids)
wr_season_stats = wr_season_stats.loc[wr_season_stats[2] == "WR"]
# wr_season_stats = wr_season_stats.loc[(wr_season_stats[2]=='WR') & (wr_season_stats[2]=='RB')]
wr_season_stats.rename(
    columns={
        0: "Player ID",
        1: "Name",
        2: "Position",
        # receiving
        3: "Air Yards",
        4: "Yards Per Reception",
        5: "Broken Tackles Receiving",
        6: "Catchable Passes Dropped",
        7: "Total Dropped Passes",
        8: "Longest Reception",
        9: "Longest TD Reception",
        10: "Receptions",
        11: "Redzone Targets",
        12: "Targets",
        13: "TD Receptions",
        14: "Reception Yards",
        15: "Yards After Catch",
        16: "Yards After Contact Receiving",
        # rushing
        17: "Scrambles",
        18: "Rushing Attempts",
        19: "Yards Per Rush",
        20: "Broken Tackles Rushing",
        21: "Kneel Downs",
        22: "Longest Rush",
        23: "Longest TD Run",
        24: "Redzone Rushing Attempts",
        25: "Negative Rushes",
        26: "Yards Lost Rushing",
        27: "Rushing Touchdowns",
        28: "Total Rushing Yards",
        29: "Yards After Contact Rushing",
        # fumbles
        30: "Fumbles",
        31: "Fumbles Lost",
    },
    inplace=True,
)

wr_season_stats


# # Top targeted WRS

# In[37]:


wr_top_targets = wr_season_stats[
    [
        "Name",
        "Targets",
        "Redzone Targets",
        "Receptions",
        "Reception Yards",
        "TD Receptions",
    ]
]
wr_top_targets = wr_top_targets[(wr_top_targets["Redzone Targets"] > 15)]
wr_top_targets = wr_top_targets.sort_values("Targets", ascending=False)
wr_top_targets


# In[38]:


avg_redzone_targets = wr_season_stats["Redzone Targets"].mean()
avg_targets = wr_season_stats["Targets"].mean()


# In[32]:


names = wr_top_targets["Name"]
total_target = wr_top_targets["Targets"] - wr_top_targets["Redzone Targets"]
redzone_target = wr_top_targets["Redzone Targets"]

bottom_total_target = redzone_target
fig, ax = plt.subplots(figsize=(20, 10))

p1 = ax.bar(
    names, total_target, bottom=redzone_target, label="Total Targets", color="#0a376b"
)
p2 = ax.bar(names, redzone_target, label="Redzone Targets", color="#25aed9")

plt.ylabel("Times Targeted", fontsize=18)
plt.xticks(fontsize=12)
plt.yticks(fontsize=14)
plt.title("Top WRs in Redzone Targets & Total Targets", fontsize=20)

ax.axhline(avg_targets, label="Average Targets in NFL", color="red")
ax.axhline(avg_redzone_targets, label="Average Redzone Targets in NFL", color="#ffad00")
plt.legend(fontsize=16)
plt.show()
