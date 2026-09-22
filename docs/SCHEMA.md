# Catalog schema

`datasets.csv` is the source of truth for this repository.

## Required fields

| Field | Rule |
|---|---|
| `id` | Stable lowercase kebab-case identifier |
| `name` | Canonical or commonly accepted dataset/resource name |
| `resource_type` | `dataset`, `archive`, `benchmark`, or `competition` |
| `tasks` | Semicolon-separated research tasks |
| `domain` | Semicolon-separated application domains |
| `series_structure` | Human-readable structural description |
| `multivariate` | `yes`, `no`, or `varies` |
| `license` | Upstream license or an explicit pointer to upstream terms |
| `access` | Public, open access, competition platform, registration, etc. |
| `source_url` | Canonical/primary URL whenever possible |
| `last_verified` | ISO date (`YYYY-MM-DD`) |

## Optional but strongly preferred fields

| Field | Meaning |
|---|---|
| `parent_collection` | Archive or benchmark family containing the dataset |
| `frequency` | Sampling cadence; semicolon-separate multiple cadences |
| `num_series` | Number of time series, channels, entities, recordings, or datasets |
| `min_length` / `max_length` | Sequence length where meaningful |
| `missing_values` | `yes`, `no`, `varies`, or `see source` |
| `citation_url` | DOI, paper, or recommended citation page |
| `notes` | Short factual research note |

## Normalization rules

- Unknown is better than guessed.
- Do not infer a dataset license from a code repository license.
- Prefer a canonical institutional page over a mirror.
- If a benchmark republishes a dataset, preserve the benchmark as `parent_collection` and avoid pretending it is the canonical origin.
- Use semicolons inside multi-value fields so commas remain safe for normal CSV quoting.
- `last_verified` means the source metadata was manually checked on that date; it does not imply the URL will remain live forever.
