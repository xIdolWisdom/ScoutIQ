[README.md](https://github.com/user-attachments/files/34395396/README.md)
# ScoutIQ

**Research-driven soccer scouting analytics and experimental sports technology.**

ScoutIQ is a soccer analytics portfolio project exploring how
event data, statistical modeling, and interactive applications
can support player evaluation.

The project currently consists of a deployed analytics
application and a separate experimental hardware concept.

## Explore ScoutIQ

- **Project website:** https://xidolwisdom.github.io/ScoutIQ/
- **Live Analytics dashboard:** https://scoutiq-analytics.streamlit.app/
- **Analytics documentation:** [analytics/README.md](analytics/README.md)
- **Research methodology:** [Methodology](analytics/research/methodology.md)
- **Research findings:** [Findings](analytics/research/findings.md)

## ScoutIQ Analytics

A Python and Streamlit scouting application built using
StatsBomb open event data.

The research dataset contains 200 player-club profiles
from the 2015/16 Premier League and La Liga.

### Features

- Passing Index V2 player leaderboards
- Individual scouting profiles
- League-specific, role-relative evaluation
- Bootstrap-based passing accuracy reliability estimates
- Barcelona longitudinal passing analysis
- Transparent research methodology and limitations

### Passing Index V2

The index combines four role-relative percentile components:

| Metric | Weight |
|---|---:|
| Progressive completed passes per 90 | 40% |
| Progressive passing accuracy | 25% |
| Overall passing accuracy | 15% |
| Passes per 90 | 20% |

Rankings are calculated separately within each league.
Scores should not be directly compared across leagues.

Bootstrap analysis uses 10,000 replicates to estimate
passing accuracy uncertainty, not uncertainty in
Passing Index V2 scores or rankings.

For detailed scoring, reliability, and reproducibility,
see the [Research Methodology](analytics/research/methodology.md).
For descriptive results and player case studies,
see the [Research Findings](analytics/research/findings.md).
For application setup, see the [Analytics README](analytics/README.md).

## ScoutIQ Lab

ScoutIQ Lab is an experimental sports technology concept
exploring an ESP32-based passing-drill measurement system.

ScoutIQ Lab is a separate experimental development track.
It is not presented as a deployed or validated hardware
measurement system on the public Analytics website.

Analytics and Lab are separate development tracks.

## Technology

**Analytics:** Python, Pandas, PyArrow, Streamlit,
StatsBomb open event data.

**Website:** HTML, CSS, JavaScript, GitHub Pages.

**Lab concept:** ESP32 and sensor-based sports measurement.

## Project Status

- ScoutIQ Analytics research MVP: complete
- Streamlit Analytics dashboard: deployed
- GitHub Pages project website: deployed
- ScoutIQ Lab: experimental prototype/concept

## Research Limitations

ScoutIQ Analytics uses historical event data and
role-relative scoring assumptions.

League-specific ranking populations are not directly
comparable. Bootstrap uncertainty applies only to
passing accuracy, and the Barcelona longitudinal
study has incomplete match coverage in some seasons.

## Repository Structure

```text
ScoutIQ/
├── index.html
├── styles.css
├── script.js
├── README.md
└── analytics/
    ├── app.py
    ├── requirements.txt
    ├── README.md
    ├── .streamlit/
    │   └── config.toml
    └── data/
        ├── players.parquet
        └── barcelona.parquet
```

## Data Attribution

Research uses StatsBomb Open Data.
See the Analytics documentation for details.

## License

License selection pending.
