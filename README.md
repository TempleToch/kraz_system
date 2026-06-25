# KRAZ Recruitment Intelligence Platform

An end-to-end data engineering and business intelligence platform for extracting, processing, ranking, and visualizing recruitment agency data.

## Project Summary

The KRAZ Recruitment Intelligence Platform automates the collection and processing of recruitment agency information from the Polish KRAZ registry.

The system extracts agency records through API-based data collection, cleans and standardizes the data, identifies agencies that provide services for foreign workers, ranks leads based on predefined business rules, and generates outreach-ready datasets for recruitment and business development activities.

A Streamlit dashboard provides real-time visibility into pipeline outputs, lead statistics, and agency intelligence.

## Key Features

* Automated API-based data extraction
* Data cleansing and normalization
* Foreign-worker recruitment agency identification
* Lead ranking and prioritization
* Outreach dataset preparation
* Interactive Streamlit dashboard
* Pipeline automation
* Data quality controls
* Deduplication and filtering

## Technology Stack

### Data Engineering

* Python
* Pandas
* Requests
* OpenPyXL

### Business Intelligence

* Streamlit
* Data Visualization
* Lead Scoring
* KPI Reporting

### Automation

* Pipeline Orchestration
* Automated Data Processing
* Batch Execution
* Logging and Monitoring

## Pipeline Architecture

1. Extract recruitment agency records
2. Normalize and validate source data
3. Filter agencies serving foreign workers
4. Score and prioritize leads
5. Generate outreach-ready datasets
6. Display results through an interactive dashboard

## Project Structure

extractor.py
Data extraction from KRAZ API

normalize.py
Data cleaning and standardization

check_foreigners.py
Agency filtering and classification

rank_leads_v2.py
Lead scoring and prioritization

prepare_outreach.py
Outreach dataset generation

dashboard.py
Business intelligence dashboard

run_pipeline.py
End-to-end pipeline execution

## Business Value

The platform reduces manual lead research effort by automating the identification and prioritization of recruitment agencies relevant to international workforce placement.

## Dashboard Features

* Pipeline status monitoring
* Lead intelligence metrics
* Agency search functionality
* Outreach dataset insights
* Automated refresh capability

## Future Enhancements

* Cloud deployment
* PostgreSQL integration
* Automated scheduling
* Email outreach automation
* Advanced lead scoring models
* Interactive geospatial analytics

## Author

Temple Tochukwu
BSc Geology | Data Engineering | Business Intelligence | Automation
