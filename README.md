# Serene_Scents_Financial_Forecasting
This project involves the development of a dynamic financial engine used to transition an early-stage consumer venture (Serene Scents) from a manual, small-batch production baseline to a scalable, data-driven enterprise.

By leveraging Python (Pandas & NumPy), the model simulates 6 months of operations, incorporating real-world variables such as seasonal demand spikes, capacity constraints, and strategic cost optimizations.

Key Business Objectives
Profitability Modeling: Established a 1.5x revenue margin rule to ensure sustainable unit economics.

Cost Optimization: Modeled a 15% reduction in production costs (from ₹129.70 to ₹110.25) through projected scale efficiencies.

Demand Forecasting: Integrated a "Festival Boost" algorithm to account for 50% demand surges during peak periods (e.g., Diwali).

Capacity Planning: Implemented operational caps (130 units/day) to simulate realistic manufacturing limits and prevent stockouts.

Technical Stack
Language: Python 3.x

Data Manipulation: pandas

Numerical Simulation: numpy

Outputs: Automated CSV generation for P&L reporting.

Analysis & Impact
Based on the simulation and actual growth data:

Revenue Growth: Modeled a 15x increase in daily revenue, scaling from ₹1,170 to a peak of ₹18,525.

Margin Expansion: Demonstrated how a 15% decrease in COGS, combined with seasonal volume, increases daily profit potential from ~₹400 to over ₹8,000.

Operational Success: Managed the resource allocation logic for a total volume exceeding 2,500 units over a 6-month period.

Repository Structure
forecasting_model.py: The core Python engine containing the growth logic and financial parameters.

serene_scents_july_realworld.csv: The generated output ledger containing daily projections (Date, Units, Cost, Revenue, Profit).

Financial_Plan.docx: The original strategic baseline used to inform the model's parameters.

How to Run
Clone the repository:

Bash
git clone https://github.com/your-username/repo-name.git
Install dependencies:

Bash
pip install pandas numpy
Execute the model:

Bash
python forecasting_model.py
Author: D Abhishek


Focus: Economics, Financial Modeling, and Strategic Consulting.
