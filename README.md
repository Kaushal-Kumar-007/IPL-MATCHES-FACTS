# 🏏 IPL Dataset Analysis

## 📌 Project Overview
This project explores the **Indian Premier League (IPL)** using two datasets:
1. **matches.csv** – Match-level details (season, teams, venue, winner, etc.)
2. **deliveries.csv** – Ball-by-ball details (runs, wickets, extras, partnerships, etc.)

The goal is to analyze IPL matches and uncover patterns in team performance, batting partnerships, bowling trends, and player contributions.

---

## 📂 Dataset Description

### **matches.csv**
| Column | Description |
|--------|-------------|
| id | Match ID (primary key) |
| season | IPL season |
| city | City where match was played |
| date | Date of the match |
| match_type | Type of match |
| player_of_match | Best performing player |
| venue | Stadium/venue |
| team1, team2 | Competing teams |
| toss_winner | Toss winning team |
| toss_decision | Bat/bowl decision |
| winner | Winning team |
| result | Match result (normal, tie, etc.) |
| result_margin | Margin of victory |
| target_runs, target_overs | Applicable in chases |
| super_over | Yes/No |
| umpire1, umpire2 | Match officials |

### **deliveries.csv**
| Column | Description |
|--------|-------------|
| match_id | Match identifier |
| inning | Inning number |
| batting_team, bowling_team | Teams involved |
| over, ball | Ball details |
| batter, bowler, non_striker | Players involved |
| batsman_runs | Runs by batter |
| extra_runs | Runs from extras |
| total_runs | Total runs (batter + extras) |
| extras_type | Type of extra (wide, no-ball, etc.) |
| is_wicket | Whether a wicket fell |
| player_dismissed | Name of dismissed player |
| dismissal_kind | Type of dismissal |
| fielder | Fielder involved |

---

## 📊 Exploratory Data Analysis (Graphs & Insights)

### 🔥 Player of the Match Awards
  
- **AB de Villiers (25 awards)** leads the chart, followed by **Chris Gayle (22)** and **Rohit Sharma (19)**.  
- Shows how individual brilliance shaped multiple matches.

---

### 👬 Top Batting Partnerships
  
- Highest partnership: **AB de Villiers & Virat Kohli (229 runs)**.  
- Other strong pairs: KL Rahul – Q de Kock, Warner – Bairstow, Gilchrist – Marsh.  
- Highlights the impact of consistent partnerships on team totals.

---

### 🏏 Dismissal Types
 
- **Caught** is the most common dismissal mode.  
- Followed by **Bowled** and **LBW**.  
- Suggests batters take aerial risks, and bowlers use full deliveries effectively.

---

### 📈 Runs per Over
  
- Most overs yield between **14–16 runs** consistently.  
- Confirms the "death overs acceleration" trend in T20 cricket.

---

### ⚠️ Extras Contribution
  
- **Wides contribute the most extra runs**, followed by **Leg Byes** and **No Balls**.  
- Bowling discipline plays a huge role in restricting runs.

---

### 🎯 Dot Ball Specialists  
- **Bhuvneshwar Kumar**: 1793 dot balls  
- **Sunil Narine**: 1694  
- **R. Ashwin**: 1623  
- **Jasprit Bumrah**: 1397  
- **Piyush Chawla**: 1337  
- Dot balls show bowling pressure applied consistently.

---

## 📝 Key Insights
- **Star Performers:** AB de Villiers, Chris Gayle, and Rohit Sharma dominate match awards.  
- **Winning Partnerships:** Kohli–AB de Villiers stand out as record breakers.  
- **Bowling Impact:** Dot-ball kings like Bhuvneshwar & Narine play pivotal roles.  
- **Scoring Trends:** Runs spike in the final overs (death overs).  
- **Discipline Factor:** Extras, especially wides, contribute significantly to team totals.  

---

## ⚙️ Tech Stack
- **Python** (Pandas, NumPy)  
- **Matplotlib & Seaborn** for data visualization  
- **Jupyter Notebook** for interactive analysis  

---

## 🚀 Future Work
- Predictive modeling: Match winners & player performances.  
- Player comparison dashboards.  
- Venue-specific strategy analysis.  

---

## 🙌 Acknowledgments
Dataset source: Kaggle IPL datasets.  
Inspired by cricket analytics projects worldwide.  

---
