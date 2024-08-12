# Questions:
1. **Drugs** 
    * Drug Use Disorders are on the rise from 2010-2017, within our 140 country sample range.
    * Given our line graph representing top 5 countries with Drug use disorder rates, why has the US increased in such fashion in contrast to the rest? Are variables that correlate with increased Drug disorder rates that could explain USA's ranking and deterioration in terms of mental health?
        * Top 5 Line Graph
        * BoxPlot or Bar Chart for GovB vs Drugs
    * Search US Drug use articles
        * NYT API
2. **Alcohol**
    * Top 5 countries are all within Eastern Europe, what characteristics do they exhibit that would explain the concentration of high alcohol use disorder rates in this regino of world?
        * HVPlot of Top 10 and Bottom 10 via GeoApify API (marker intensity by disorder rate)... or just chart for extremes
        * *TBD Visualisation??*
    * Does legal drinking age limits have impact on alcohol use disorder rates? All top 5 countries had legal drinking age limits of 18 during 2010-2017 period
        * Bar chart comparison of Wine, Beer, and Spirit categories by Age limit vs. Alcohol disorder rate
3. **Anxiety**
    * The Top and Bottom 5 are grossly disparate in terms of economic status. Is anxiety related to economic environment?
        * Linear Regression of GDP per Capita vs Anxiety disorder. -> more money more problems? Mongolia?
        * Linear Regression of Life Expectancy vs Anxiety disorder. -> increase life expectancy at birth, inreased anxiety disorder rates? Mongolia?
        * Linear Regressino Urban Pop Ratio vs Anxiety Disorder Rate
        * *TBD Visualisation??*
4. **Depression**
    * Gender Prevalence in Females. Why so?
        * Pie Chart
        * TBD Visualisation!
5. **Eating**
    * Eating Disorders are on the rise from 2010-2017, within our 140 country sample range.
        * With increase in urbanisation, could this be facilitating increase in Eating Disorder Rates? - Linear Regression Urban Pop Ratio vs Eating (r^2 = 0.5!!!)
    * Why is thare a moderate positive correlation between Eating Disorders rates and Percentage GDP Expenditure on healthcare? could it be with increased facilities or medical personnel comes increased awareness and likelihood of diagnosis?
        * Linear regression HealthExp vs Eating
        * TBD Visualisation!
6. **Schiz**
    * Mental Health History?
    * Schiz vs Age Dependency Ratio????
7. **Bipolar**
    * Bipolar Disordrs are on the rise from 2010-2017, within our 140 country sample range.
        * With increase in urbanisation, coudl this be facilitating increase in Bipolar Disorder Rates? - Linear Regression Urban Pop Ratio vs Bipolar (r^2 = 0.4!!!)




























## Sorting and Top & Bottom Lines
**Depression(%)**  
* Top 5: Lesotho, Morocco, Uganda, Finland, United States  
* Bottom 5: Albania, Colombia, Peru, Poland, Myanmar  
**Anxiety(%)**  
* Top 5: New Zealand, Norway, United States, France, Australia  
* Bottom 5: Colombia, Tajikistan, Mongolia, Uzbekistan, Turkmenistan  
**Drugs(%)**  
* Top 5: United States, United Arab Emirates, Afghanistan, Libya, Canada  
* Bottom 5: Burkina Faso, Bosnia and Herzegovina, Mali, Guinea, Chad  
**Alcohol(%)**  
* Top 5: Belarus, Estonia, Ukraine, Lithuania, Latvia  
* Bottom 5: Italy, Israel, Japan, Morocco, Malaysia  
**Eating(%)**  
* Top 5: Australia, Luxembourg, Spain, Austria, New Zealand  
* Bottom 5: Liberia, Central African Republic, Solomon Islands, Niger, Malawi  
**Schizophrenia(%)**  
* Top 5: Netherlands, Australia, New Zealand, United Stated, China  
* Bottom 5: Central African Republic, Malawi, Mozambique, Zimbabwe, Uganda  
**Bipolar(%)**  
* Top 5: New Zealand, Australia, Brazil, United Kingdom, Paraguay  
* Bottom 5: China, Papua New Guinea, Vanuatu, Solomon Islands, Fiji 


General Guidelines for R-squared Values
	1.	Social Sciences and Health Research:
	▪	An R² value of 0.10 to 0.30 is often considered low but can still be meaningful, indicating that while there is some relationship, a lot of variance in mental disorder rates is influenced by other factors not included in the model.
	▪	An R² value of 0.30 to 0.50 indicates a moderate relationship and is generally considered acceptable for social science research, suggesting that GDP per capita does explain a notable portion of the variance in mental disorder rates.
	▪	An R² value of 0.50 and above indicates a strong relationship, suggesting that GDP per capita is a significant predictor of mental disorder rates.


## %GDP Health Exp vs Disorder Rates  
* Eating Disorder:  
    * r^2 = 0.31399644901081714  
    * y = 0.04x + 0.02  
* Bipolar Disorder:  
    * r^2 = 0.21612929875854656  
    * y = 0.03x + 0.55  
* Anxiety Disorder:  
    * r^2 = 0.20522750017817143  
    * y = 0.21x + 2.65  



* Depression
    * OpenWeatherAPI (Avg weather stats like sun exposure -> impact on Depression)?????????  
    * Depression Gender Prevalence - F: 59.7 vs M: 40.3
* Anxiety
    * GDP per capita vs Anxiety -> r^2 = 0.4 -> With more money comes more problems?
    * GDP Health Exp vs Anxiety -> r^2 = 0.2
    * Life Expectancy vs Anxiety -> r^2 = 0.3


An off-premise legal drinking age limit of 18 seems to perform the worst in terms of alcohol disorder rate. Note, the top 5 countires in alcohol disorders had legal drinking ages of 18 during 2010-2017, with Lithuania lifting it to 20 in 2018, and Latvia proposing an increase to 20.




