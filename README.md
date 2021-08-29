# capstone-dataengineeringnd

In this project, we will demonstrate how to build a data warehouse that enriches the analysis of frequently occurring events by augmenting the event data with ancillary information. Actual process and summary is described in the notebook (capstone_project.ipynb).

## description of files
- capstone_project.ipynb: This notebook contains the detailed description of the project, the data dictionary and the actual ETL process demonstration.
- db.cfg: The configuration file of our database.
- create_tables.py, sql_queries.py: Scripts used in the DB initialization and ETL process.
- \*.SAS: The SAS description file accompanied with the dataset which describes the specification of immigrations data.
- immigration_data_sample.csv: The sample of immigrations data which is the sources of fact table.
- us-cities-demographics.csv, airport-codes_csv.csv: The ancillary datasets which are sources of dimension table.
  - Note that the temperature dataset is not uploaded in the repository because its original size is too large.

