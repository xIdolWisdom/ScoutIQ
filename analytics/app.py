
import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="ScoutIQ Analytics",
    page_icon="⚽",
    layout="wide"
)

APP_DIR = Path(__file__).resolve().parent

DATA_PATH = APP_DIR / "data" / "players.parquet"

@st.cache_data
def load_players(file_path, file_mtime_ns):
    return pd.read_parquet(file_path)

players = load_players(
    str(DATA_PATH),
    DATA_PATH.stat().st_mtime_ns
)

st.title("⚽ ScoutIQ Analytics")

st.caption(
    "Research-driven soccer passing and scouting analytics"
)

st.sidebar.header("Navigation")

page = st.sidebar.radio(
    "Explore ScoutIQ",
    [
        "Overview",
        "Leaderboard",
        "Player Profiles",
        "Barcelona Longitudinal",
        "Research"
    ]
)

st.sidebar.divider()

st.sidebar.link_button(
    "↗ ScoutIQ Main Website",
    "https://xidolwisdom.github.io/ScoutIQ/"
)


if page == "Overview":

    st.header("Scouting Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Player-Club Profiles",
        len(players)
    )

    col2.metric(
        "Leagues",
        players["league"].nunique()
    )

    col3.metric(
        "Season",
        "2015/16"
    )

    st.subheader("Dataset Coverage")

    st.dataframe(
        players.groupby("league")
        .size()
        .rename("Profiles")
        .reset_index(),
        hide_index=True,
        width="stretch"
    )

    st.info(
        "Passing Index V2 rankings are calculated "
        "within each league's comparison population. "
        "Scores should not be interpreted as "
        "directly comparable across leagues."
    )

elif page == "Leaderboard":

    st.header("Passing Index V2 Leaderboard")

    league = st.selectbox(
        "Select league",
        sorted(players["league"].unique())
    )

    filtered = players[
        players["league"] == league
    ].copy()

    roles = sorted(
        filtered["role"].dropna().unique()
    )

    selected_roles = st.multiselect(
        "Filter by role",
        roles,
        default=roles
    )

    search = st.text_input(
        "Search player or club"
    ).strip().casefold()

    filtered = filtered[
        filtered["role"].isin(selected_roles)
    ]

    if search:
        filtered = filtered[
            filtered["player_search"].str.contains(
                search,
                regex=False,
                na=False
            )
            |
            filtered["team_search"].str.contains(
                search,
                regex=False,
                na=False
            )
        ]

    display_columns = {
        "league_rank": "League Rank",
        "player_name": "Player",
        "team": "Club",
        "role": "Role",
        "passing_index_v2": "Passing Index V2",
        "passes_per90": "Passes / 90",
        "pass_accuracy_pct": "Pass Accuracy (%)",
        "progressive_passes_per90": "Progressive Passes / 90"
    }

    filtered = filtered.sort_values(
        ["league_rank", "player_name", "team"]
    )

    st.dataframe(
        filtered[
            list(display_columns)
        ].rename(
            columns=display_columns
        ),
        hide_index=True,
        width="stretch"
    )

    st.caption(
        "Original league ranks are preserved "
        "when applying filters."
    )

elif page == "Player Profiles":

    st.header("Player Passing Profiles")

    options = players.sort_values(
        ["player_name", "league", "team"]
    )

    record_ids = options["record_id"].tolist()

    labels = {
        row["record_id"]:
            f"{row['player_name']} — "
            f"{row['team']} ({row['league']})"
        for _, row in options.iterrows()
    }

    selected_id = st.selectbox(
        "Select a player-club profile",
        record_ids,
        format_func=lambda record_id: labels[record_id]
    )

    player = players.loc[
        players["record_id"] == selected_id
    ].iloc[0]

    st.subheader(player["player_name"])

    st.write(
        f"**Club:** {player['team']}  "
        f"| **League:** {player['league']}  "
        f"| **Role:** {player['role']}"
    )

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Passing Index V2",
        f"{player['passing_index_v2']:.2f}"
    )

    c2.metric(
        "League Rank",
        f"#{int(player['league_rank'])}"
    )

    c3.metric(
        "Pass Accuracy",
        f"{player['pass_accuracy_pct']:.1f}%"
    )

    st.subheader("Passing Metrics")

    metrics = pd.DataFrame({
        "Metric": [
            "Passes per 90",
            "Progressive Passes per 90",
            "Progressive Pass Accuracy",
            "Minutes",
            "Role Stability"
        ],
        "Value": [
            f"{player['passes_per90']:.2f}",
            f"{player['progressive_passes_per90']:.2f}",
            f"{player['progressive_accuracy_pct']:.1f}%",
            f"{player['minutes']:.1f}",
            str(player["role_stability"])
        ]
    })

    st.dataframe(
        metrics,
        hide_index=True,
        width="stretch"
    )

    st.subheader("Scouting Reliability")

    st.caption(
        "Match-level bootstrap intervals based on "
        "10,000 resamples of observed matches."
    )

    r1, r2, r3 = st.columns(3)

    r1.metric(
        "Matches Observed",
        f"{int(player['matches_observed']):,}"
    )

    r2.metric(
        "Total Passes",
        f"{int(player['total_passes']):,}"
    )

    r3.metric(
        "Progressive Pass Attempts",
        f"{int(player['progressive_attempts_v2']):,}"
    )

    reliability_table = pd.DataFrame({
        "Metric": [
            "Overall Pass Accuracy",
            "Progressive Pass Accuracy"
        ],
        "Observed (%)": [
            player["pass_accuracy_pct"],
            player["progressive_accuracy_pct"]
        ],
        "Bootstrap Lower (%)": [
            player["pass_boot_ci_lower"],
            player["progressive_boot_ci_lower"]
        ],
        "Bootstrap Upper (%)": [
            player["pass_boot_ci_upper"],
            player["progressive_boot_ci_upper"]
        ]
    })

    st.dataframe(
        reliability_table.round(2),
        hide_index=True,
        width="stretch"
    )

    st.info(
        "These bootstrap intervals describe uncertainty "
        "in passing accuracy. They are not confidence "
        "intervals for the Passing Index V2 score "
        "or league rank."
    )

    st.caption(
        f"Bootstrap replicates: "
        f"{int(player['bootstrap_replicates']):,}"
    )


elif page == "Barcelona Longitudinal":

    st.header("Barcelona Longitudinal Study")

    st.caption(
        "Observed StatsBomb matches, 2014/15–2017/18. "
        "This descriptive study is separate from "
        "the league-relative Passing Index V2."
    )

    @st.cache_data
    def load_barcelona(file_path, file_mtime_ns):
        return pd.read_parquet(file_path)

    barcelona_path = (
        APP_DIR / "data" / "barcelona.parquet"
    )

    longitudinal = load_barcelona(
        str(barcelona_path),
        barcelona_path.stat().st_mtime_ns
    )

    player_options = (
        longitudinal[["player_id", "player_name"]]
        .drop_duplicates()
        .sort_values("player_name")
    )

    player_labels = dict(
        zip(
            player_options["player_id"],
            player_options["player_name"]
        )
    )

    selected_player_id = st.selectbox(
        "Select Barcelona player",
        player_options["player_id"].tolist(),
        format_func=lambda value: player_labels[value]
    )

    history = (
        longitudinal.loc[
            longitudinal["player_id"] == selected_player_id
        ]
        .sort_values("season")
        .copy()
    )

    st.subheader(player_labels[selected_player_id])

    display = history[
        [
            "season",
            "midfield_minutes",
            "midfield_share_pct",
            "dominant_role",
            "passes_per90",
            "pass_accuracy_pct",
            "progressive_passes_v2_per90",
            "progressive_accuracy_v2"
        ]
    ].rename(
        columns={
            "season": "Season",
            "midfield_minutes": "Midfield Minutes",
            "midfield_share_pct": "Midfield Share (%)",
            "dominant_role": "Dominant Role",
            "passes_per90": "Passes / 90",
            "pass_accuracy_pct": "Pass Accuracy (%)",
            "progressive_passes_v2_per90":
                "Progressive Passes / 90",
            "progressive_accuracy_v2":
                "Progressive Accuracy (%)"
        }
    )

    st.dataframe(
        display.round(2),
        hide_index=True,
        width="stretch"
    )

    st.subheader("Season Coverage")

    coverage = history[
        [
            "season",
            "total_minutes",
            "midfield_minutes",
            "midfield_share_pct",
            "total_passes",
            "progressive_attempts_v2"
        ]
    ].rename(
        columns={
            "season": "Season",
            "total_minutes": "Observed Minutes",
            "midfield_minutes": "Midfield Minutes",
            "midfield_share_pct": "Midfield Share (%)",
            "total_passes": "Pass Attempts",
            "progressive_attempts_v2":
                "Progressive Attempts"
        }
    )

    st.dataframe(
        coverage.round(2),
        hide_index=True,
        width="stretch"
    )

    st.warning(
        "Coverage limitation: these figures describe "
        "observed matches, not necessarily complete "
        "league seasons. Coverage is incomplete in "
        "2016/17 and 2017/18. Changes in playing role "
        "and observed minutes can affect comparisons."
    )

    st.info(
        "This study does not assign league-wide "
        "Passing Index V2 ranks to Barcelona "
        "player-season profiles."
    )

else:

    st.header("Research & Methodology")

    st.markdown("""
    ### Passing Index V2

    ScoutIQ evaluates midfield passing performance
    using a frozen, role-relative scoring methodology.

    **Index components:**

    - 40% progressive completed passes per 90
    - 25% progressive pass accuracy
    - 15% overall pass accuracy
    - 20% total passes per 90

    ### Research Scope

    - Premier League 2015/16: 98 player-club profiles
    - La Liga 2015/16: 102 player-club profiles
    - Reliability research includes match-level bootstrap analysis
    - Barcelona longitudinal research is maintained separately

    ### Important Limitations

    Rankings are descriptive, not predictions.

    League-relative scores are not directly comparable
    across different league populations.

    Historical data does not represent current-season form.
    """)

st.divider()

st.caption(
    "ScoutIQ Analytics | Historical research prototype"
)
