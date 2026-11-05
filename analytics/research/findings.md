# ScoutIQ Analytics — Research Findings

## Research Scope

This report summarizes descriptive findings from 200
eligible player-club profiles in the 2015/16 Premier
League and La Liga seasons.

The population includes 98 Premier League profiles
and 102 La Liga profiles across 40 clubs.

Passing Index V2 scores are calculated using
league-specific, role-relative percentile ranks.
Scores should not be compared directly across leagues.

## Finding 1 — Tactical Roles Exhibit Different Passing Profiles

Across the combined research population, Attacking/Wide
midfielders recorded lower mean values than Central
and Defensive Midfield players on all four passing
components. These pooled summaries describe the
observed profiles; they are not cross-league index
comparisons.

| Metric | Attacking/Wide | Central | Defensive |
|---|---:|---:|---:|
| Mean passes per 90 | 43.03 | 50.62 | 51.58 |
| Mean pass accuracy | 73.69% | 81.21% | 81.57% |
| Mean progressive passes per 90 | 6.52 | 8.20 | 8.57 |
| Mean progressive accuracy | 56.41% | 61.74% | 61.18% |

These are descriptive differences. They do not
establish differences in underlying player ability.

## Finding 2 — Median Results Reinforce Role Differences

Median progressive passes per 90 were:

- Attacking/Wide: 5.94
- Central Midfield: 8.51
- Defensive Midfield: 7.88

The Attacking/Wide group's 75th percentile (7.83)
was below the median of both other groups.

The distributions nevertheless overlap.

## Finding 3 — League-Specific Patterns Vary

La Liga Central Midfield profiles recorded a median
progressive accuracy of 69.18%, compared with 58.48%
among Premier League Central Midfield profiles.

The respective sample sizes were 11 and 22.

This observed difference should not be interpreted
as a general league-wide advantage or a causal effect.

## Finding 4 — Exposure Is Associated With Interval Width

Across all 200 profiles, Pearson correlations were:

| Exposure measure | Interval measure | Correlation |
|---|---|---:|
| Progressive attempts | Progressive accuracy CI width | -0.738 |
| Total passes | Overall accuracy CI width | -0.688 |
| Observed matches | Progressive accuracy CI width | -0.605 |
| Observed matches | Overall accuracy CI width | -0.493 |

Greater observed exposure generally accompanied
narrower bootstrap accuracy intervals.

These are descriptive associations consistent with
the construction of the uncertainty estimates.

## Finding 5 — Progressive Accuracy Has Wider Intervals

Median 95% bootstrap interval widths, in percentage
points, were:

| Role | Overall accuracy | Progressive accuracy |
|---|---:|---:|
| Attacking/Wide | 5.97 | 12.56 |
| Central Midfield | 5.09 | 10.80 |
| Defensive Midfield | 5.57 | 11.70 |

These intervals quantify uncertainty under resampling
of observed player-matches.

They do not represent uncertainty in Passing Index V2
scores or rankings.

## Finding 6 — High Rankings Do Not Guarantee Narrow Intervals

Top-ten profiles generally exhibited narrower median
progressive accuracy intervals than their respective
full-league populations.

| League | Top-ten median width | League median width |
|---|---:|---:|
| La Liga | 10.92 pp | 12.37 pp |
| Premier League | 9.09 pp | 11.24 pp |

However, individual high-ranked profiles still
displayed meaningfully different uncertainty widths.

Index scores and progressive interval widths had
Pearson correlations of -0.451 in La Liga and
-0.483 in the Premier League.

These associations do not establish predictive validity.

## Player Case Studies

### Toni Kroos — High Performance and Narrower Uncertainty

- League: La Liga
- Published rank: 1
- Passing Index V2: 100.00
- Progressive passes per 90: 15.46
- Progressive accuracy: 84.87%
- Progressive accuracy 95% bootstrap interval:
  82.39% to 87.48%
- Observed progressive attempts: 575
- Observed matches: 32
- Role stability: Clear

### Marcelo Díaz — High Rank, Wider Uncertainty

- League: La Liga
- Published rank: 4
- Passing Index V2: 95.28
- Progressive accuracy: 75.24%
- Progressive accuracy 95% bootstrap interval:
  67.52% to 81.94%
- Observed progressive attempts: 206
- Observed matches: 14
- Role stability: Clear

### James Rodríguez — Role Classification Stability

- League: La Liga
- Published rank: 3
- Passing Index V2: 96.18
- Assigned role: Attacking/Wide
- Role stability: Close
- Role margin: 8.87 percentage points

The stability label describes reconstructed tactical
deployment. It is not a confidence interval or
statistical probability.

No alternative-role scoring experiment was conducted
for this player.

### Santi Cazorla — Progression and Role Stability

- League: Premier League
- Published rank: 2
- Passing Index V2: 94.77
- Progressive passes per 90: 17.09
- Progressive accuracy: 75.07%
- Observed matches: 15
- Role stability: Moderate

### Cesc Fàbregas — High Progression Volume

- League: Premier League
- Published rank: 5
- Passing Index V2: 85.70
- Progressive passes per 90: 21.22
- Observed progressive attempts: 1,034
- Observed matches: 37
- Role stability: Moderate

## Interpretation

The results illustrate the value of reporting
passing progression, accuracy, tactical role,
sample exposure, and statistical precision
as distinct analytical dimensions.

Passing Index V2 provides a descriptive,
role-relative composite of passing characteristics.
It does not measure overall player quality.

## Limitations

- The findings describe two historical league seasons.
- Player-club profiles are observational units.
- Tactical roles are broad classifications.
- Passing outcomes reflect tactical and team context.
- Some league-role groups have small sample sizes.
- Correlations are descriptive, not causal.
- Bootstrap intervals describe observed-match
  resampling uncertainty only.
- Predictive validity has not been established.
- Scores are not directly comparable across leagues.

## Reproducibility

The frozen scoring and ranking layer was independently
reconstructed for all 200 published profiles.

All nine archived research artifacts matched their
recorded SHA-256 checksums.

Complete upstream raw-event processing reproducibility
has not yet been independently demonstrated.

## Data Attribution

Research uses StatsBomb open event data.

This document is an unpublished research findings
draft prepared during ScoutIQ Day 15.
