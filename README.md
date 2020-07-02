# Ironhack Data Analyrics Module 1 Project README file

Survey answers Pipeline showing quantity and percentage of respondents per country, job and living area.

---

### :computer: **Technology stack**
Python

### :boom: **Core technical concepts and inspiration**
Reporting tool to analyze survey results.

It will generate a .csv updated every time the script runs.

### :wrench: **Configuration**
See needed libraries in: requirements.txt.

Database used can be found in: /data/raw/raw_data_project_m1.db.

### :see_no_evil: **Usage**
When running the script it will export all countries by default. 

In case filtering by one or more countries is needed, run the script using `-c or --country` parameters including a blank space between each country as shown below:

`python main_script -c Spain Austria`

The script will export a .csv per each stage of the project which you'll find in the /data folder.

### :file_folder: **Folder structure**
```
└── project
    ├── __trash__
    ├── .gitignore
    ├── .env
    ├── requeriments.txt
    ├── README.md
    ├── main_script.py
    ├── notebooks
    │   ├── Acquire_Wrangling_Functions.ipynb
    │   └── Analysis_Functions.ipynb
    ├── p_acquisition
    │   └── m_acquisition.py
    ├── p_analysis
    │   └── m_analysis.py
    ├── p_wrangling
    │   └── m_wrangling.py
    └── data
        ├── raw
        ├── processed
        └── results
``` 

### :information_source: **Further info**
Web Scraping link: https://iban.com/country-codes

---

