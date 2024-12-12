Fraud Analysis Dashboard - TrustGuard Insurance
Project Overview
This project involves creating a Power BI dashboard to analyze fraudulent claims for TrustGuard Insurance. The dashboard provides insights into fraud trends, customer demographics, and geographic hotspots to help optimize fraud detection, resource allocation, and operational efficiency.

Features
The dashboard includes the following key visuals:

Total Claims and Fraud by Incident Type
Identifies incident types with the highest fraud rates.
Fraud by Customer Demographics
Explores the relationship between customer demographics and fraudulent claims.
Fraud Hotspots
Maps geographic regions with the highest concentration of fraudulent claims.
Fraud by Claim Characteristics
Analyzes fraud trends based on claim amounts, police reports, and property damage.
Temporal Patterns of Fraud
Highlights when fraudulent claims are most likely to occur (seasonal or weekly patterns).
Policy Risk Assessment
Examines policies with high fraud rates based on deductibles and coverage levels.
Fraud by Vehicle Characteristics
Identifies vehicle makes and models associated with higher fraud rates.
Claims with Inconsistent Features
Flags claims with missing or inconsistent data for further investigation.
Business Objectives
The project aims to:

Reduce fraudulent payouts by identifying high-risk claims and customers.
Optimize resource allocation for fraud detection teams.
Enhance operational efficiency by fast-tracking legitimate claims.
Inform policy adjustments to minimize future fraud risks.
Data Fields
The dataset includes the following columns:

Customer Information: months_as_customer, age, insured_education_level, insured_occupation, insured_hobbies, insured_relationship.
Policy Details: policy_number, policy_bind_date, policy_state, policy_csl, policy_deductable, policy_annual_premium, umbrella_limit.
Incident Details: incident_date, incident_type, collision_type, incident_severity, authorities_contacted, incident_state, incident_city, incident_hour_of_the_day.
Claim Details: total_claim_amount, injury_claim, property_claim, vehicle_claim.
Vehicle Details: auto_make, auto_model, auto_year.
Fraud Indicator: fraud_reported.
Setup Instructions
Prerequisites
Power BI Desktop (Free Tier)
A CSV or Excel file containing the provided dataset.
Steps to Create the Dashboard
Load the Data:
Import the dataset into Power BI Desktop.
Create Visuals:
Follow the detailed visual creation steps outlined in the project document.
Publish to Power BI Service:
Save the report and publish it to the Power BI Service.
Pin visuals to create an interactive dashboard.
Share the Dashboard:
Share the dashboard link with stakeholders or team members.
Visuals and Business Insights
Total Claims and Fraud by Incident Type

Business Value: Focuses on incident types with the highest fraud rates to prioritize investigations.
Analytical Insight: E.g., "Theft" claims have a 60% fraud rate, suggesting the need for stricter verification protocols.
Fraud by Customer Demographics

Business Value: Reveals demographic groups more prone to fraud, guiding verification strategies.
Analytical Insight: E.g., High school-educated males in specific occupations report 70% more fraudulent claims.
Fraud Hotspots

Business Value: Identifies regions with concentrated fraud activity for targeted resource allocation.
Analytical Insight: E.g., Los Angeles reports 30% of fraudulent claims, prompting localized fraud mitigation efforts.
Fraud by Claim Characteristics

Business Value: Detects trends in high-value claims with missing documentation, aiding in fraud detection.
Analytical Insight: Claims above $50,000 without police reports have a 90% fraud likelihood.
Temporal Patterns of Fraud

Business Value: Highlights seasonal or weekly spikes in fraud, enabling proactive resource planning.
Analytical Insight: Fraud increases by 50% during the holiday season, suggesting the need for heightened scrutiny.
Policy Risk Assessment

Business Value: Adjusts policies to mitigate risks associated with high-fraud segments.
Analytical Insight: Policies with low deductibles and high coverage limits show a 40% higher fraud rate.
Fraud by Vehicle Characteristics

Business Value: Guides underwriting decisions by identifying high-risk vehicle makes and models.
Analytical Insight: Luxury brands like "BMW" show a 25% higher fraud rate than the average.
Claims with Inconsistent Features

Business Value: Flags inconsistent claims for detailed review, improving fraud detection accuracy.
Analytical Insight: Property damage claims of $100,000 without witnesses or police reports are disproportionately fraudulent.
Additional Notes
Limitations: This dashboard does not include advanced machine learning or predictive analysis but focuses on descriptive insights based on historical data.
Future Enhancements: Integration with Python/R scripts for predictive fraud detection or anomaly detection models.
Contact
For questions or support, please contact:

Name: Sithabiseni Mtshali
Email: sithabisenimtshali@gmail.com
