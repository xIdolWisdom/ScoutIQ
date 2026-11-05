# ScoutIQ Analytics

A research-driven soccer scouting application built with Python, Pandas, and Streamlit.

## Live Dashboard

https://scoutiq-analytics.streamlit.app/

## Overview

ScoutIQ evaluates midfield passing performance using StatsBomb open event data.
The application includes 200 player-club profiles from the 2015/16 Premier League and La Liga.

## Features

- Scouting overview and dataset coverage
- Passing Index V2 leaderboards
- Individual player-club scouting profiles
- Bootstrap-based passing reliability analysis
- Barcelona longitudinal passing study
- Research methodology and limitations

## Research Documentation

- [Research Methodology](research/methodology.md)
- [Research Findings](research/findings.md)

The published scoring and ranking layer has been
independently reconstructed for all 200 profiles.
Archived research artifact integrity has been
verified against nine recorded SHA-256 checksums.
The complete upstream raw-event processing pipeline
has not yet been independently reproduced.

## Passing Index V2

| Component | Weight |
|---|---:|
| Progressive completed passes per 90 | 40% |
| Progressive passing accuracy | 25% |
| Overall passing accuracy | 15% |
| Passes per 90 | 20% |

Scores use role-relative percentiles. Rankings are calculated within each league.
Scores and rankings should not be directly compared across leagues.

## Reliability

Passing accuracy uncertainty is estimated using 10,000 bootstrap replicates.
These estimates do not quantify uncertainty in index scores or rankings.

## Barcelona Longitudinal Study

A descriptive analysis of four Barcelona players across the 2014/15–2017/18 seasons.
Match coverage is incomplete in some seasons, particularly 2016/17 and 2017/18.
This analysis does not produce league-wide Passing Index V2 rankings.

## Data

Source: StatsBomb Open Data.

- data/players.parquet
- data/barcelona.parquet

## Installation

Install a compatible Python version, then run:

    pip install -r requirements.txt

## Run Locally

    streamlit run app.py

## Technology

- Python
- Pandas
- PyArrow
- Streamlit
- StatsBomb open event data

## Project Status

Research MVP complete. Streamlit dashboard deployed.

## Limitations

- Historical event-data coverage
- Role-relative scoring assumptions
- League-specific ranking populations
- Bootstrap intervals limited to passing accuracy
- Incomplete longitudinal season coverage

## License

License selection pending.
