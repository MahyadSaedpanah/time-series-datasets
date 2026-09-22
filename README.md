# Time Series Dataset Hub

A research-oriented catalog of public time-series datasets, archives, and benchmarks for **forecasting, classification, anomaly detection, regression, representation learning, and signal analysis**.

> **Scope:** this repository indexes canonical or well-documented sources. It does **not** re-upload third-party datasets unless redistribution is explicitly permitted.

## Why this repository exists

Time-series datasets are scattered across university archives, competition pages, benchmark repositories, and domain-specific data portals. This project keeps a structured, research-friendly index with explicit provenance, access, and licensing metadata.

The source of truth is [`datasets.csv`](datasets.csv). The catalog below is generated from that file.

## Catalog

<!-- CATALOG:START -->

### Archives & collections

| Resource | Tasks | Domain | Structure | Frequency | Scale | Access / license |
|---|---|---|---|---|---|---|
| [UCR Time Series Classification Archive](https://www.timeseriesclassification.com/) | classification, clustering | multiple | univariate dataset collection | varies | 128 datasets | public; Varies by constituent dataset/source |
| [UEA Multivariate Time Series Classification Archive](https://www.timeseriesclassification.com/) | classification | multiple | multivariate dataset collection | varies | 30 datasets | public; Varies by constituent dataset/source |
| [Time Series Extrinsic Regression Archive](https://www.timeseriesclassification.com/) | regression | multiple | time-series regression dataset collection | varies | — | public; Varies by constituent dataset/source |
| [Monash Time Series Forecasting Archive](https://forecastingdata.org/) | forecasting | multiple | forecasting dataset collection | varies | — | public; Varies by constituent dataset/source |

### Forecasting

| Resource | Tasks | Domain | Structure | Frequency | Scale | Access / license |
|---|---|---|---|---|---|---|
| [M1](https://forecastingdata.org/) | forecasting | multiple | collection of time series | yearly;quarterly;monthly | 1001; len 15–150 | public via Monash archive; See original dataset/source terms linked by Monash |
| [M3](https://forecastingdata.org/) | forecasting | multiple | collection of time series | yearly;quarterly;monthly;other | 3003; len 20–144 | public via Monash archive; See original dataset/source terms linked by Monash |
| [M4](https://forecastingdata.org/) | forecasting | multiple | collection of time series | yearly;quarterly;monthly;weekly;daily;hourly | 100000; len 19–9933 | public via Monash archive; See original dataset/source terms linked by Monash |
| [Tourism](https://forecastingdata.org/) | forecasting | tourism | collection of time series | yearly;quarterly;monthly | 1311; len 11–333 | public via Monash archive; See original dataset/source terms linked by Monash |
| [CIF 2016](https://forecastingdata.org/) | forecasting | banking | collection of time series | monthly | 72; len 34–120 | public via Monash archive; See original dataset/source terms linked by Monash |
| [London Smart Meters](https://forecastingdata.org/) | forecasting | energy | collection of time series | — | 5560; len 288–39648 | public via Monash archive; See original dataset/source terms linked by Monash |
| [Australian Electricity Demand](https://forecastingdata.org/) | forecasting | energy | collection of time series | — | 5; len 230736–232272 | public via Monash archive; See original dataset/source terms linked by Monash |
| [Wind Farms](https://forecastingdata.org/) | forecasting | energy | collection of time series | — | 339; len 6345–527040 | public via Monash archive; See original dataset/source terms linked by Monash |
| [Dominick](https://forecastingdata.org/) | forecasting | sales | collection of time series | weekly | 115704; len 28–393 | public via Monash archive; See original dataset/source terms linked by Monash |
| [Bitcoin](https://forecastingdata.org/) | forecasting | economic | collection of time series | — | 18; len 2659–4581 | public via Monash archive; See original dataset/source terms linked by Monash |
| [Pedestrian Counts](https://forecastingdata.org/) | forecasting | transport | collection of time series | hourly | 66; len 576–96424 | public via Monash archive; See original dataset/source terms linked by Monash |
| [Vehicle Trips](https://forecastingdata.org/) | forecasting | transport | collection of time series | — | 329; len 70–243 | public via Monash archive; See original dataset/source terms linked by Monash |
| [KDD Cup 2018](https://forecastingdata.org/) | forecasting | nature | collection of time series | — | 270; len 9504–10920 | public via Monash archive; See original dataset/source terms linked by Monash |
| [Weather](https://forecastingdata.org/) | forecasting | nature | collection of time series | daily | 3010; len 1332–65981 | public via Monash archive; See original dataset/source terms linked by Monash |
| [NN5](https://forecastingdata.org/) | forecasting | banking | collection of time series | daily;weekly | 111; len 791–791 | public via Monash archive; See original dataset/source terms linked by Monash |
| [Web Traffic](https://forecastingdata.org/) | forecasting | web | collection of time series | daily;weekly | 145063; len 803–803 | public via Monash archive; See original dataset/source terms linked by Monash |
| [Solar](https://forecastingdata.org/) | forecasting | energy | collection of time series | 10-minute;weekly | 137; len 52560–52560 | public via Monash archive; See original dataset/source terms linked by Monash |
| [Electricity](https://forecastingdata.org/) | forecasting | energy | collection of time series | hourly;weekly | 321; len 26304–26304 | public via Monash archive; See original dataset/source terms linked by Monash |
| [Car Parts](https://forecastingdata.org/) | forecasting | sales | collection of time series | — | 2674; len 51–51 | public via Monash archive; See original dataset/source terms linked by Monash |
| [FRED-MD](https://forecastingdata.org/) | forecasting | economic | collection of time series | monthly | 107; len 728–728 | public via Monash archive; See original dataset/source terms linked by Monash |
| [San Francisco Traffic](https://forecastingdata.org/) | forecasting | transport | collection of time series | hourly;weekly | 862; len 17544–17544 | public via Monash archive; See original dataset/source terms linked by Monash |
| [Rideshare](https://forecastingdata.org/) | forecasting | transport | collection of time series | — | 2304; len 541–541 | public via Monash archive; See original dataset/source terms linked by Monash |
| [Hospital](https://forecastingdata.org/) | forecasting | health | collection of time series | monthly | 767; len 84–84 | public via Monash archive; See original dataset/source terms linked by Monash |
| [COVID Deaths](https://forecastingdata.org/) | forecasting | health, epidemiology | collection of time series | daily | 266; len 212–212 | public via Monash archive; See original dataset/source terms linked by Monash |
| [Temperature Rain](https://forecastingdata.org/) | forecasting | climate, environment | collection of time series | — | 32072; len 725–725 | public via Monash archive; See original dataset/source terms linked by Monash |
| [Sunspot](https://forecastingdata.org/) | forecasting | climate, astronomy | single time series | — | 1; len 73931–73931 | public via Monash archive; See original dataset/source terms linked by Monash |
| [Saugeen River Flow](https://forecastingdata.org/) | forecasting | climate, hydrology | single time series | daily | 1; len 23741–23741 | public via Monash archive; See original dataset/source terms linked by Monash |
| [US Births](https://forecastingdata.org/) | forecasting | demography | single time series | daily | 1; len 7305–7305 | public via Monash archive; See original dataset/source terms linked by Monash |
| [Electricity Transformer Temperature (ETT-small)](https://github.com/zhouhaoyi/ETDataset) | forecasting | energy | multivariate | 15-minute;hourly | 4 benchmark files | public repository; See upstream repository terms |
| [Individual Household Electric Power Consumption](https://archive.ics.uci.edu/dataset/235/individual+household+electric+power+consumption) | regression, clustering, forecasting | energy | multivariate time series | 1-minute | 1 household; len 2075259–2075259 | public; CC BY 4.0 |
| [Appliances Energy Prediction](https://archive.ics.uci.edu/dataset/374/appliances+energy+prediction) | regression, forecasting | energy, smart home | multivariate time series | 10-minute | 1 building; len 19735–19735 | public; CC BY 4.0 |
| [Beijing Multi-Site Air Quality](https://archive.ics.uci.edu/dataset/501/beijing) | regression, forecasting | climate, environment | multivariate multi-site time series | hourly | 12 monitoring sites | public; CC BY 4.0 |
| [Bike Sharing](https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset) | regression, forecasting | transport, mobility | multivariate temporal demand data | hourly;daily | 1 system; len 17389–17389 | public; CC BY 4.0 |
| [Metro Interstate Traffic Volume](https://archive.ics.uci.edu/dataset/492/metro+interstate+traffic+volume) | regression, forecasting | transport, traffic | multivariate sequential time series | hourly | 1 road segment; len 48204–48204 | public; CC BY 4.0 |
| [Seoul Bike Sharing Demand](https://archive.ics.uci.edu/dataset/560/seoul+bike+sharing+demand) | regression, forecasting | transport, mobility | multivariate temporal demand data | hourly | 1 system; len 8760–8760 | public; CC BY 4.0 |
| [SML2010](https://archive.ics.uci.edu/dataset/274/sml2010) | regression, forecasting | smart home, environment | multivariate sequential time series | 15-minute means | 1 monitored house; len 4137–4137 | public; See UCI dataset page |
| [Power Consumption of Tetouan City](https://archive.ics.uci.edu/dataset/849/power+consumption+of+tetouan+city) | regression, forecasting | energy | multivariate time series | 10-minute | 3 power zones; len 52416–52416 | public; CC BY 4.0 |
| [Air Quality](https://archive.ics.uci.edu/dataset/360/air+quality) | regression, forecasting | climate, environment, sensors | multivariate time series | hourly | 1 sensor deployment; len 9358–9358 | public; CC BY 4.0 |

### Classification & regression

| Resource | Tasks | Domain | Structure | Frequency | Scale | Access / license |
|---|---|---|---|---|---|---|
| [Human Activity Recognition Using Smartphones](https://archive.ics.uci.edu/dataset/240/human+activity+recognition+using+smartphones) | classification, clustering | human activity, sensors | multivariate inertial-sensor windows | 50 Hz | 30 subjects | public; CC BY 4.0 |
| [Condition Monitoring of Hydraulic Systems](https://archive.ics.uci.edu/dataset/447/condition+monitoring+of+hydraulic+systems) | classification, regression | industrial, sensors | multivariate cyclic sensor time series | mixed: 1–100 Hz | 2,205 load cycles | public; CC BY 4.0 |
| [BIDMC PPG and Respiration Dataset](https://physionet.org/content/bidmc/1.0.0/) | signal analysis, regression | healthcare, PPG, respiration | multivariate physiological waveforms | 125 Hz signals;1 Hz numerics | 53 recordings; len 8 minutes–8 minutes | open access; Open Data Commons Attribution License v1.0 |
| [Sleep-EDF Database Expanded](https://physionet.org/content/sleep-edfx/1.0.0/) | classification, signal analysis | healthcare, sleep, EEG | multivariate polysomnography | mixed | 197 whole-night recordings | open access; See PhysioNet license terms |

### Anomaly detection

| Resource | Tasks | Domain | Structure | Frequency | Scale | Access / license |
|---|---|---|---|---|---|---|
| [Numenta Anomaly Benchmark (NAB)](https://github.com/numenta/NAB) | anomaly detection | multiple | timestamped univariate streams | varies | 58 files | public repository; See repository license and source-specific terms |
| [SMAP Spacecraft Telemetry](https://github.com/khundman/telemanom) | anomaly detection | spacecraft, telemetry | multivariate telemetry channels | anonymized | 55 telemetry channels | public via linked dataset; See upstream dataset terms |
| [MSL Spacecraft Telemetry](https://github.com/khundman/telemanom) | anomaly detection | spacecraft, telemetry | multivariate telemetry channels | anonymized | 27 telemetry channels | public via linked dataset; See upstream dataset terms |
| [Server Machine Dataset (SMD)](https://github.com/NetManAIOps/OmniAnomaly) | anomaly detection | IT operations, server telemetry | multivariate server metrics | see source | 28 machines | public repository; See repository/data terms |

### Physiological signals

| Resource | Tasks | Domain | Structure | Frequency | Scale | Access / license |
|---|---|---|---|---|---|---|
| [MIT-BIH Arrhythmia Database](https://physionet.org/content/mitdb/1.0.0/) | classification, signal analysis, anomaly detection | healthcare, ECG | 2-channel physiological waveforms | 360 Hz | 48 half-hour recordings | open access; Open Data Commons Attribution License v1.0 |
| [MIMIC-IV Waveform Database v0.1.0](https://physionet.org/content/mimic4wdb/0.1.0/) | signal analysis, representation learning, clinical prediction | healthcare, ICU | multivariate physiological waveforms and numerics | mixed | 200 records / 198 patients | open access; See PhysioNet license terms |

<!-- CATALOG:END -->

## Metadata schema

See [`docs/SCHEMA.md`](docs/SCHEMA.md) for field definitions and normalization rules.

## Inclusion criteria

A resource should satisfy most of the following:

1. It has a canonical or primary source.
2. It is publicly documented and accessible, even if registration is required.
3. Its provenance is clear enough for research use.
4. It has a paper, DOI, official documentation, or an established benchmark role.
5. License/access conditions can be identified or linked.
6. It adds meaningful coverage of a task, domain, data characteristic, or benchmark family.

Mirrors should not replace canonical sources. Preprocessed copies may be listed only when their relationship to the original data is documented.

## Reproducibility

Validate the catalog:

```bash
python scripts/validate_catalog.py
```

Regenerate the README catalog:

```bash
python scripts/build_readme.py
```

Check that the README is in sync without modifying it:

```bash
python scripts/build_readme.py --check
```

## Contributing

Contributions are welcome. Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) before opening a pull request.

## Licensing and attribution

The original catalog metadata and documentation in this repository are released under **CC0-1.0**.

**Dataset licenses are not inherited from this repository.** Each dataset, archive, benchmark, or competition remains governed by its original license, citation requirements, privacy restrictions, competition rules, and access policy.

## Citation

If this catalog is useful in a paper or project, cite the repository using [`CITATION.cff`](CITATION.cff). For scientific work, also cite the original dataset authors and papers.

## Roadmap

- Expand high-quality anomaly-detection benchmarks.
- Add finance/economics datasets with canonical licensing information.
- Add distribution-shift and domain-adaptation metadata.
- Add lightweight automated link-status reporting.
- Tag benchmark variants separately from canonical dataset sources.

---

**v0.2:** curated breadth with provenance first. Quantity is not a substitute for source quality.
