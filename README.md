# Finding Safer Neighborhoods in San Francisco

## Aim
This project identifies relatively safer neighborhoods in San Francisco by analyzing traffic crash incident data and grouping neighborhoods based on incident counts.

## Data Source
San Francisco Open Data Portal traffic crash dataset, saved locally as `data/raw/sf_data.csv`.

## Data Mining Task
This project uses clustering analysis with K-means to group neighborhoods into low-, medium-, and high-incident categories.

## Preprocessing
- Loaded the CSV dataset
- Selected the `analysis_neighborhood` column
- Removed missing values
- Counted the number of incidents per neighborhood

## How to Run
1. Install dependencies:

```bash
py -m pip install -r requirements.txt

used the following to run the code
	-py src/main.py

Output

The program creates:

output/neighborhood_safety.csv

output/cluster_summary.csv

It also displays a bar chart of the top 10 neighborhoods by incident count.

Findings

The project ranks neighborhoods by incident count and groups them into clusters. Lower-incident clusters may represent relatively safer neighborhoods, while higher-incident clusters indicate greater incident activity.

Course Relevance

This project applies clustering, a data mining technique, to real-world public safety data from San Francisco.

Acknowledgment

I used AI for guidance and debugging on certain things I couldn't figure out.