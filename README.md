# KRAZ Recruitment Intelligence Platform

An end-to-end data engineering and business intelligence platform built to extract, process, analyze, and prioritize recruitment agencies from Poland's KRAZ registry.

## Live Demo

Streamlit Dashboard: (https://kraz-intelligence-vaad5qulvch34yebrzhxqx.streamlit.app/)

## Overview

The KRAZ Recruitment Intelligence Platform automates the collection and analysis of recruitment agency data from the Polish KRAZ registry.

The platform extracts agency records, cleans and standardizes data, identifies agencies serving foreign workers, ranks leads, and produces outreach-ready datasets for recruitment and business development activities.

## Key Features

* Automated extraction of KRAZ agency records
* Data normalization and cleansing
* Foreign-worker agency identification
* Lead ranking and prioritization
* Outreach-ready dataset generation
* Interactive Streamlit dashboard
* Search and filtering capabilities
* Downloadable lead datasets

## Technology Stack

* Python
* Pandas
* Streamlit
* OpenPyXL
* Requests
* Playwright
* Git & GitHub

## Data Pipeline

1. Extract agency data from KRAZ registry
2. Normalize and clean records
3. Identify agencies serving foreign workers
4. Rank agencies using lead-scoring logic
5. Generate outreach-ready datasets
6. Visualize results through Streamlit dashboard

## Project Structure

```text
kraz-intelligence/
│
├── dashboard.py
├── extractor.py
├── normalize.py
├── check_foreigners.py
├── rank_leads_v2.py
├── prepare_outreach.py
├── run_pipeline.py
│
├── data/
│   ├── demo_foreigners.xlsx
│   ├── demo_ranked_leads.xlsx
│   └── demo_outreach.xlsx
│
├── requirements.txt
└── README.md
```

## Results

* 7,655+ agency records processed
* 2,208 agencies identified as serving foreign workers
* 2,022 ranked recruitment leads generated
* 1,595 outreach-ready leads prepared

## Dashboard Preview

Add screenshots here.

## Installation

```bash
pip install -r requirements.txt
streamlit run dashboard.py
```

## Skills Demonstrated

* Data Engineering
* ETL Development
* Data Cleaning
* Data Quality Management
* Business Intelligence
* Dashboard Development
* Automation
* Git Version Control

## Future Enhancements

* Interactive visual analytics
* Docker deployment
* Automated scheduling
* PostgreSQL integration
* Lead scoring optimization

## Author

Temple Tochukwu
BSc Geology | Data Engineering | Business Intelligence | Automation
