Motivation:
Suicide is a global phenomenon; in fact, 78% of suicides occurred in low- and middle-income countries in 2015.
Death by suicide is an extremely complex issue that causes pain to hundreds of thousands of people every year around the world.
According to estimates from the World Health Organization (WHO), Suicide is the second leading cause of death among 15-29 years old and over 800,000 people die because of it every year.
Such large numbers motivated us to work on this topic.
This corresponds to an age-standardized suicide rate of around 11.5 per 100,000 people – a figure equivalent to someone dying of suicide every 40 seconds. Yet suicides are preventable with timely, evidence-based interventions.

Hypothesis:
Can different factors related to a country’s living conditions predict the suicide rate in the country?

Retrieving the Data:
There are problems with availability and accuracy of data about suicides. The data that will be explored and described in the notebook was obtained from the source:
·       Csv file source: https://www.kaggle.com/russellyates88/suicide-rates-overview-1985-to-2016
·       APIsource:https://raw.githubusercontent.com/datasets/geo-countries/master/data/countries.geojson

Cleaning and uploading the dataset into Database

Data Exploration:
The goal of this data exploration process is to visualize the trends and patterns in the dataset available and observing the changes in patterns over the years by country, sex and gdp.

Data Visualizations:
#### Interactive choropleth map with hover – by city and suicide number
#### Line chart – number of suicides by age
#### Bar chart – Top 10 countries by number of suicides
#### Pie chart – Male vs Female suicide rate
#### Scatter plot – check for correlation between GDP and number of suicides
#### Scatter plot – Y- axis – beginning year of dataset, X-axis – ending year of our dataset

Data Analysis:
1)    We started with exploratory analysis and plotted each variable against suicide rate , just to discover that there were no strong correlations.
2)    But we found out that even though none of the variables have a strong direct impact , altogether they might have an effect!

Summary and Conclusions:
Suicide is indeed one of the most talked about issue in these crisis times and this research helped us to check the influence of multiple factors such as poverty, mental health, unemployment and many more. We wish to continue our research and help people in knowing the exact leading causes of suicide so that it is much easier to prevent it and help those who are close to committing it. But the reason behind suicide can’t be easily identified. Each country has its different social and cultural background that leads to different reasons for suicide.

Interesting Facts: 
While we were exploring and researching on this study we have discovered the other factors like sunshine hours per year and alcohol consumption contributes to suicide.

Components Used:
Database – PostgreSQL – Generated by Python Script, Table created from csv file
Flask – python code, connects to PostgreSQL, retrieves the data from PostgreSQL, Serves data in JSON format via endpoints
Landing Page – index.html - custom CSS files,
Data Visualization (Libraries used) – java script, D3.js, Plotly, D3,geomap/JQuery with Ajax (new library)

Link to access the dashboard, which has the "Charts and Maps" page with the visualizations.If you click on any of the links from the slider and you can explore the charts. 
https://globalsuiciderates.herokuapp.com