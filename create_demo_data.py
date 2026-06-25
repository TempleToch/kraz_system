import pandas as pd

ranked = pd.read_excel(
    "data/foreigners_ranked_leads_v2.xlsx"
)

outreach = pd.read_excel(
    "data/outreach_ready_leads.xlsx"
)

foreigners = pd.read_excel(
    "data/foreigners_agencies.xlsx"
)

ranked.head(100).to_excel(
    "data/demo_ranked_leads.xlsx",
    index=False
)

outreach.head(100).to_excel(
    "data/demo_outreach.xlsx",
    index=False
)

foreigners.head(100).to_excel(
    "data/demo_foreigners.xlsx",
    index=False
)

print("Demo datasets created")