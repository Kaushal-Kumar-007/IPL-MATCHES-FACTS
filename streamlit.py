import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
matches = pd.read_csv("MATCHESIPL.csv")
deliveries = pd.read_csv("DELIVERIESIPL.csv")

# Streamlit app title
st.title("IPL Data Analysis Dashboard")

# Example: Matches per season
matches_per_season = matches.groupby('season').size()

fig, ax = plt.subplots()
matches_per_season.plot(kind='bar', ax=ax, color='skyblue')
ax.set_title("Matches Per Season")
ax.set_xlabel("Season")
ax.set_ylabel("Matches")
st.pyplot(fig)  # <-- Show matplotlib figure in Streamlit





import streamlit as st
import matplotlib.pyplot as plt

# Streamlit section title
st.header("Matches Per Venue")

# Group by venue and count matches
matches_per_venue = matches.groupby('venue').size().reset_index(name='matches')

# Sort by matches in descending order
matches_per_venue = matches_per_venue.sort_values('matches', ascending=False)

# Plotting
fig, ax = plt.subplots(figsize=(10,10))
bars = ax.bar(matches_per_venue['venue'], matches_per_venue['matches'], color='lightgreen')

# Add labels on bars
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height, str(int(height)),
            ha='center', va='bottom', fontsize=9, fontweight='bold')

ax.set_xlabel('Venue')
ax.set_ylabel('Number of Matches')
ax.set_title('Matches per Venue')
ax.set_xticks(range(len(matches_per_venue['venue'])))
ax.set_xticklabels(matches_per_venue['venue'], rotation=90)

fig.tight_layout()  # Prevent label cutoff

# Display in Streamlit
st.pyplot(fig)


import streamlit as st
import matplotlib.pyplot as plt

# Streamlit section title
st.header("Overall Wins by Team")

# Count wins per team
wins_by_team = matches['winner'].value_counts().reset_index()
wins_by_team.columns = ['team', 'wins']

# Plotting
fig, ax = plt.subplots(figsize=(10,6))
bars = ax.bar(wins_by_team['team'], wins_by_team['wins'], color='orange')

# Add labels on bars
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height, str(int(height)),
            ha='center', va='bottom', fontsize=9, fontweight='bold')

ax.set_xlabel('Team')
ax.set_ylabel('Number of Wins')
ax.set_title('Overall Wins by Team')
ax.set_xticks(range(len(wins_by_team['team'])))
ax.set_xticklabels(wins_by_team['team'], rotation=90)

fig.tight_layout()  # Prevent label cutoff

# Display in Streamlit
st.pyplot(fig)

import streamlit as st
import matplotlib.pyplot as plt

# Streamlit section title
st.header("Wins by Team per Season")

# Group by season and winner to count wins
wins_per_season = matches.groupby(['season', 'winner']).size().reset_index(name='wins')

# Pivot for plotting
pivot_df = wins_per_season.pivot(index='season', columns='winner', values='wins').fillna(0)

# Create the figure and plot
fig, ax = plt.subplots(figsize=(14,6))
pivot_df.plot(kind='bar', stacked=False, ax=ax, colormap='tab20')

ax.set_xlabel('Season')
ax.set_ylabel('Number of Wins')
ax.set_title('Wins by Team per Season')
ax.legend(title='Team', bbox_to_anchor=(1.05, 1), loc='upper left')

fig.tight_layout()

# Display in Streamlit
st.pyplot(fig)


import streamlit as st
import matplotlib.pyplot as plt

# Streamlit section title
st.header("Toss Decision Counts (Bat vs Field)")

# Count toss decisions
toss_decision_counts = matches['toss_decision'].value_counts().reset_index()
toss_decision_counts.columns = ['decision', 'count']

# Create the figure and plot
fig, ax = plt.subplots(figsize=(6,5))
bars = ax.bar(toss_decision_counts['decision'], toss_decision_counts['count'], color=['blue', 'green'])

# Add labels on bars
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height, str(int(height)),
            ha='center', va='bottom', fontsize=10, fontweight='bold')

ax.set_xlabel('Toss Decision')
ax.set_ylabel('Number of Times Chosen')
ax.set_title('Toss Decision Counts (Bat vs Field)')

# Display in Streamlit
st.pyplot(fig)




import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Section title
st.header("Impact of Toss on Match Result")

# Count matches where toss winner also won the match
same_winner_count = (matches['toss_winner'] == matches['winner']).sum()
total_matches = len(matches)

# Calculate percentage
percentage = (same_winner_count / total_matches) * 100
st.write(f"**Toss winner also won match:** {same_winner_count} out of {total_matches} matches ({percentage:.2f}%)")

# Prepare data for plotting
data = pd.DataFrame({
    'Outcome': ['Toss Winner Won', 'Toss Winner Lost'],
    'Count': [same_winner_count, total_matches - same_winner_count]
})

# Plot
fig, ax = plt.subplots(figsize=(6,5))
bars = ax.bar(data['Outcome'], data['Count'], color=['purple', 'red'])

# Add labels on bars
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height, str(int(height)),
            ha='center', va='bottom', fontsize=10, fontweight='bold')

ax.set_xlabel('Match Outcome')
ax.set_ylabel('Number of Matches')
ax.set_title('Impact of Toss on Match Result')

# Display in Streamlit
st.pyplot(fig)


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Section title
st.header("Player of the Match Frequency")

# Count frequency of each Player of the Match
player_of_match_freq = matches['player_of_match'].value_counts().reset_index()
player_of_match_freq.columns = ['player_of_match', 'count']

# Show the top 10 in the table
st.subheader("Top 10 Players of the Match")
st.dataframe(player_of_match_freq.head(10))

# Plot top 10 players
top10_players = player_of_match_freq.head(10)

fig, ax = plt.subplots(figsize=(10,6))
bars = ax.bar(top10_players['player_of_match'], top10_players['count'], color='gold')

# Add labels on bars
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height, str(int(height)),
            ha='center', va='bottom', fontsize=9, fontweight='bold')

ax.set_xlabel('Player')
ax.set_ylabel('Number of Awards')
ax.set_title('Top 10 Players of the Match')
ax.set_xticklabels(top10_players['player_of_match'], rotation=45, ha='right')

# Display in Streamlit
st.pyplot(fig)


import streamlit as st
import matplotlib.pyplot as plt

# Section title
st.header("Top 10 Run Scorers in IPL")

# Calculate total runs scored by each batter
top_scorers = deliveries.groupby("batter")["total_runs"].sum().sort_values(ascending=False).head(10)

# Create the plot
fig, ax = plt.subplots(figsize=(10,6))
top_scorers.plot(kind="bar", color="orange", ax=ax)

ax.set_title("Top 10 Run Scorers in IPL", fontsize=16)
ax.set_xlabel("Batter", fontsize=12)
ax.set_ylabel("Total Runs", fontsize=12)
ax.set_xticklabels(top_scorers.index, rotation=45, ha="right")
ax.grid(axis="y", linestyle="--", alpha=0.7)

# Display in Streamlit
st.pyplot(fig)


import streamlit as st
import matplotlib.pyplot as plt

# Section title
st.header("Top 10 Wicket Takers in IPL")

# Filter only actual wicket deliveries (exclude run outs, retired hurt, etc.)
wicket_df = deliveries[
    (deliveries["is_wicket"] == 1) & 
    (~deliveries["dismissal_kind"].isin(["run out", "retired hurt", "obstructing the field"]))
]

# Count wickets per bowler
top_wicket_takers = wicket_df.groupby("bowler")["is_wicket"].count().sort_values(ascending=False).head(10)

# Create plot
fig, ax = plt.subplots(figsize=(10,6))
top_wicket_takers.plot(kind="bar", color="purple", ax=ax)

ax.set_title("Top 10 Wicket Takers in IPL", fontsize=16)
ax.set_xlabel("Bowler", fontsize=12)
ax.set_ylabel("Total Wickets", fontsize=12)
ax.set_xticklabels(top_wicket_takers.index, rotation=45, ha="right")
ax.grid(axis="y", linestyle="--", alpha=0.7)

# Display in Streamlit
st.pyplot(fig)


import streamlit as st
import matplotlib.pyplot as plt

# Section title
st.header("Top 10 Players by Boundary Count (4s & 6s)")

# Filter only 4s and 6s
boundaries_df = deliveries[deliveries["batsman_runs"].isin([4, 6])]

# Count boundaries per batter
boundary_counts = boundaries_df.groupby("batter")["batsman_runs"].count().sort_values(ascending=False).head(10)

# Count 4s and 6s separately for stacked plot
fours = deliveries[deliveries["batsman_runs"] == 4].groupby("batter")["batsman_runs"].count()
sixes = deliveries[deliveries["batsman_runs"] == 6].groupby("batter")["batsman_runs"].count()

top_players = boundary_counts.index
fours = fours[top_players]
sixes = sixes[top_players]

# Create figure
fig, ax = plt.subplots(figsize=(10,6))
ax.bar(top_players, fours, label="4s", color="skyblue")
ax.bar(top_players, sixes, bottom=fours, label="6s", color="orange")

# Labels and style
ax.set_title("Top 10 Players by Boundary Count (4s & 6s)", fontsize=16)
ax.set_xlabel("Batter", fontsize=12)
ax.set_ylabel("Boundary Count", fontsize=12)
ax.set_xticklabels(top_players, rotation=45, ha="right")
ax.legend()
ax.grid(axis="y", linestyle="--", alpha=0.7)

# Display in Streamlit
st.pyplot(fig)


import streamlit as st
import matplotlib.pyplot as plt

# Section title
st.header("Extras Breakdown in IPL")

# Filter only rows with extras
extras_df = deliveries[deliveries["extras_type"].notna()]

# Count each extras type
extras_count = extras_df["extras_type"].value_counts()

# Create figure
fig, ax = plt.subplots(figsize=(8,5))
extras_count.plot(kind="bar", color="teal", ax=ax)

# Labels and style
ax.set_title("Extras Breakdown in IPL", fontsize=16)
ax.set_xlabel("Extras Type", fontsize=12)
ax.set_ylabel("Count", fontsize=12)
ax.set_xticklabels(extras_count.index, rotation=45, ha="right")
ax.grid(axis="y", linestyle="--", alpha=0.7)

# Display in Streamlit
st.pyplot(fig)




import streamlit as st
import matplotlib.pyplot as plt

# Section title
st.header("Distribution of Runs per Over in IPL")

# Calculate runs per over for each match
runs_per_over = deliveries.groupby(['match_id', 'over'])['total_runs'].sum().reset_index()

# Get the over with the maximum runs
max_over = runs_per_over.loc[runs_per_over['total_runs'].idxmax()]

# Display the max over details in Streamlit
st.subheader("Most Runs in a Single Over")
st.write(f"**Match ID:** {max_over['match_id']}, **Over:** {int(max_over['over'])}, **Runs:** {max_over['total_runs']}")

# Plot histogram of runs per over
fig, ax = plt.subplots(figsize=(8,5))
ax.hist(runs_per_over['total_runs'], bins=range(0, 37), edgecolor='black', color='orange')

# Labels and style
ax.set_title("Distribution of Runs per Over in IPL", fontsize=16)
ax.set_xlabel("Runs in Over", fontsize=12)
ax.set_ylabel("Frequency", fontsize=12)
ax.grid(axis="y", linestyle="--", alpha=0.7)

# Display in Streamlit
st.pyplot(fig)


import streamlit as st
import matplotlib.pyplot as plt

# Section title
st.header("Dismissal Types Distribution in IPL")

# Filter only rows where wicket fell
dismissals_df = deliveries[deliveries["is_wicket"] == 1]

# Count each dismissal type
dismissal_counts = dismissals_df["dismissal_kind"].value_counts()

# Plot in Matplotlib
fig, ax = plt.subplots(figsize=(8,5))
dismissal_counts.plot(kind="bar", color="crimson", ax=ax)

# Labels and style
ax.set_title("Dismissal Types Distribution in IPL", fontsize=16)
ax.set_xlabel("Dismissal Type", fontsize=12)
ax.set_ylabel("Count", fontsize=12)
ax.set_xticklabels(dismissal_counts.index, rotation=45, ha="right")
ax.grid(axis="y", linestyle="--", alpha=0.7)

# Show in Streamlit
st.pyplot(fig)



import streamlit as st
import matplotlib.pyplot as plt

# Section title
st.header("Top 10 Bowlers by Dot Balls Bowled in IPL")

# Filter dot balls (no runs, no extras)
dot_balls_df = deliveries[(deliveries["total_runs"] == 0) & (deliveries["extras_type"].isna())]

# Count dot balls by bowler
dot_balls_count = dot_balls_df.groupby("bowler")["total_runs"].count().sort_values(ascending=False).head(10)

# Plot
fig, ax = plt.subplots(figsize=(10,6))
dot_balls_count.plot(kind="bar", color="navy", ax=ax)

# Labels and style
ax.set_title("Top 10 Bowlers by Dot Balls Bowled in IPL", fontsize=16)
ax.set_xlabel("Bowler", fontsize=12)
ax.set_ylabel("Dot Balls", fontsize=12)
ax.set_xticklabels(dot_balls_count.index, rotation=45, ha="right")
ax.grid(axis="y", linestyle="--", alpha=0.7)

# Add value labels on bars
for bar in ax.patches:
    ax.text(bar.get_x() + bar.get_width()/2, 
            bar.get_height(), 
            str(int(bar.get_height())), 
            ha='center', va='bottom', fontsize=9, fontweight='bold')

# Show in Streamlit
st.pyplot(fig)





import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Section title
st.header("Top 10 Partnerships in IPL")

# Load dataset
df = pd.read_csv("DELIVERIESIPL.csv")

# Create a sorted tuple for each batting pair so order doesn't matter
df['pair'] = df.apply(lambda x: tuple(sorted([x['batter'], x['non_striker']])), axis=1)

# Calculate total runs for each pair in each match and innings
partnerships = df.groupby(['match_id', 'inning', 'pair'])['total_runs'].sum().reset_index()

# Get the top 10 partnerships overall
top_partnerships = partnerships.sort_values(by='total_runs', ascending=False).head(10)

# Plot
fig, ax = plt.subplots(figsize=(12,6))
ax.barh(
    [f"{p[0]} & {p[1]}" for p in top_partnerships['pair']], 
    top_partnerships['total_runs'], 
    color="goldenrod"
)
ax.set_title("Top 10 Partnerships in IPL", fontsize=16)
ax.set_xlabel("Runs", fontsize=12)
ax.invert_yaxis()  # Highest at top
ax.grid(axis="x", linestyle="--", alpha=0.7)

# Add labels to bars
for i, v in enumerate(top_partnerships['total_runs']):
    ax.text(v + 1, i, str(v), va='center', fontsize=9, fontweight='bold')

# Display in Streamlit
st.pyplot(fig)
