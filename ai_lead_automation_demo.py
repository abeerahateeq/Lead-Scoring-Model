import pandas as pd

# -------------------------------------------------
# SafeX AI Automation Demo: Automated Lead Prioritizer
# -------------------------------------------------
# A simple automation that receives incoming business leads,
# scores them, explains the score, and recommends a next action.

budget_scores = {"Low": 10, "Medium": 25, "High": 40}
urgency_scores = {"Low": 10, "Medium": 20, "High": 30}
industry_scores = {
    "Healthcare": 30,
    "Finance": 25,
    "Technology": 20,
    "Retail": 15,
    "Education": 10,
    "Manufacturing": 5,
}

sample_leads = [
    {"Lead": "Dr. Sarah - Private Clinic", "Industry": "Healthcare", "Budget": "High", "Urgency": "High"},
    {"Lead": "Ali - E-commerce Store", "Industry": "Retail", "Budget": "Medium", "Urgency": "High"},
    {"Lead": "Usman - Software Agency", "Industry": "Technology", "Budget": "High", "Urgency": "Medium"},
    {"Lead": "Ayesha - Training Academy", "Industry": "Education", "Budget": "Medium", "Urgency": "Low"},
    {"Lead": "Bilal - Small Factory", "Industry": "Manufacturing", "Budget": "Low", "Urgency": "Low"},
]


def score_lead(lead):
    budget = budget_scores.get(lead["Budget"], 0)
    urgency = urgency_scores.get(lead["Urgency"], 0)
    industry = industry_scores.get(lead["Industry"], 0)
    return budget + urgency + industry


def classify(score):
    if score >= 80:
        return "Hot"
    elif score >= 60:
        return "Warm"
    return "Cold"


def next_action(category):
    actions = {
        "Hot": "Contact within 1 hour and offer a discovery call.",
        "Warm": "Send a personalized follow-up and book a demo.",
        "Cold": "Add to nurture sequence and follow up later.",
    }
    return actions[category]


def explain_lead(lead):
    reasons = []
    if lead["Budget"] == "High":
        reasons.append("high budget")
    elif lead["Budget"] == "Medium":
        reasons.append("moderate budget")
    else:
        reasons.append("limited budget")

    if lead["Urgency"] == "High":
        reasons.append("urgent need")
    elif lead["Urgency"] == "Medium":
        reasons.append("moderate urgency")
    else:
        reasons.append("low urgency")

    reasons.append(f"{lead['Industry'].lower()} industry fit")
    return ", ".join(reasons)


results = []

print("\nSAFE X AI LEAD AUTOMATION DEMO")
print("=" * 45)
print("Incoming leads are automatically scored and prioritized.\n")

for lead in sample_leads:
    score = score_lead(lead)
    category = classify(score)

    result = {
        **lead,
        "Lead Score": score,
        "Priority": category,
        "Why": explain_lead(lead),
        "Recommended Action": next_action(category),
    }
    results.append(result)

    print(f"Lead: {lead['Lead']}")
    print(f"Score: {score}/100 | Priority: {category}")
    print(f"Why: {result['Why']}")
    print(f"Next action: {result['Recommended Action']}")
    print("-" * 45)

# Automation output: prioritize the highest-value leads first.
df = pd.DataFrame(results).sort_values("Lead Score", ascending=False)
df.to_csv("prioritized_leads.csv", index=False)

print("\nAUTOMATION COMPLETE")
print("Prioritized lead list saved as: prioritized_leads.csv\n")
print(df[["Lead", "Lead Score", "Priority", "Recommended Action"]].to_string(index=False))
