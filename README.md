# 🏏 IPL Dataset Analysis

## 📌 Project Overview
This project explores the **Indian Premier League (IPL)** through two datasets:
1. **matches.csv** – Match-level details (teams, venue, toss, results, etc.)
2. **deliveries.csv** – Ball-by-ball details (runs, wickets, extras, partnerships, etc.)

By analyzing these datasets, we uncover facts about teams, players, partnerships, dismissals, scoring patterns, extras, and bowling dominance.

---

## 📂 Dataset Description

### **matches.csv**
- Contains **1095 entries** with 20 columns.  
- Key columns: `id`, `season`, `city`, `date`, `venue`, `team1`, `team2`, `toss_winner`, `winner`, `player_of_match`, `result_margin`.

### **deliveries.csv**
- Contains **260,920 entries** with 17 columns.  
- Key columns: `match_id`, `inning`, `batting_team`, `bowling_team`, `over`, `ball`, `batter`, `bowler`, `total_runs`, `is_wicket`, `player_dismissed`, `dismissal_kind`.

---

## 📊 Analysis & Insights

### 🌟 Player Performances
- **Player of the Match Awards**    
  - **AB de Villiers (25 awards)** tops the list.  
  - Followed by **Chris Gayle (22)**, **Rohit Sharma (19)**, **Virat Kohli (18)**, and **David Warner (18)**.  
  - These players consistently changed the course of matches.

---

### 👬 Batting Partnerships
- **Best Partnerships in IPL History (by runs)**    
  - **Virat Kohli & AB de Villiers**: 229 runs and 215 runs (two different matches).  
  - **Sai Sudharsan & Shubman Gill**: 210 runs.  
  - **KL Rahul & Quinton de Kock**: 210 runs.  
  - **Gilchrist & Marsh**: 206 runs.  
  - Other strong pairs include Gayle–Kohli (204), Warner–Ojha (189), Warner–Bairstow (185), Lynn–Gambhir (184), Rahul–Agarwal (183).  
- **Key Insight:** Partnerships often dictate match outcomes, with certain duos dominating repeatedly.

---

### 🏏 Dismissals
- **Types of Dismissals**    
  - **Caught** is the most common mode of dismissal.  
  - Followed by **Bowled** and **LBW**.  
- **Key Insight:** Aerial shots carry the highest risk, making field placement critical.

---

### 📈 Scoring Trends
- **Runs per Over**    
  - Across most overs, teams score consistently between **14–16 runs**.  
  - Death overs (16–20) see acceleration, with batsmen targeting boundaries.  
- **Key Insight:** Consistency in scoring reflects aggressive T20 batting strategies.

---

### ⚠️ Extras
- **Contribution of Extras**   
  - **Wides contribute the most runs** among extras.  
  - Followed by **Leg Byes** and **No Balls**.  
- **Key Insight:** Lack of bowling discipline significantly boosts opposition totals.

---

### 🎯 Bowling Impact
- **Dot Ball Specialists**    
  - **Bhuvneshwar Kumar**: 1793 dot balls.  
  - **Sunil Narine**: 1694.  
  - **R. Ashwin**: 1623.  
  - **Jasprit Bumrah**: 1397.  
  - **Piyush Chawla**: 1337.  
- **Key Insight:** These bowlers consistently built pressure, proving invaluable in T20 where every ball counts.

---

## 📝 Summary of Facts
- **AB de Villiers** is the most impactful player (25 PoM awards).  
- **Kohli & AB de Villiers** dominate the record books with the highest partnerships.  
- **Caught dismissals** are most frequent, showing risk in aggressive batting.  
- **Scoring stability** lies between 14–16 runs per over, with spikes at the death.  
- **Wides** are the biggest extras contributor.  
- **Dot ball kings**: Bhuvneshwar Kumar, Narine, Ashwin, Bumrah, Chawla.  

---

## ⚙️ Tech Stack
- **Python** (Pandas, NumPy)  
- **Matplotlib & Seaborn** for visualization  
- **Jupyter Notebook** for exploration  

---

## 🚀 Future Enhancements
- Build predictive models (e.g., predict match winners, player of the match).  
- Compare players across eras.  
- Venue-based strategy analysis.  

---

## 🙌 Acknowledgments
Dataset sourced from **Kaggle IPL datasets**.  
Inspired by the passion for cricket analytics and T20 strategy.  

---
