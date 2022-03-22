# python_midterm_project
Project name: The weather and air pollution index

## Report on the Analysis

### Goal of the analysis:

Our goal for this project is to investigate the relationship between the air pollution index and weather variables. We want to classify and find which variables could increase or decrease the daily mean value or AQI related to people’s health of every city.

### Methodology:

The methodology of our project is to use the OLS regression models between air pollution indicators and weather variable data.

### Description and Findings:

According to the air pollution data, our group searched and used three indicators including pm2.5, pm10, NO2 from 2010 to 2021. In addition, after comparing the relevance and the integrity of cities’ weather stations, we chose airport weather stations of each city because they contain many specific numbers and values of data including Precipitation(PRCP), Average Wind Speed(AWND), Maximum Temperature(TMAX), Average Temperature(TAVG) and other types. 

For the main part, having considered the amount of data of weather types and realistic factors, we chose PRCP, AWND, TMAX, TAVG, and Snow Depth (SNWD) to run the OLS regression with three air pollution indicators. Then we picked up four representative and significant tables of OLS regression from the log table of weather factors from 30 tables. 

Firstly, for the OLS regression table of “Dallas Daily Mean NO2 Concentration” and “PRCP, AWND, and TMAX”, from the table, when PRCP increases about 1%, the daily mean NO2 concentration will decrease by about 0.287 units. When AWND increases 1%, the daily mean NO2 concentration will decrease by 6.7907 units. The daily mean NO2 concentration will decrease by approximately 1.8275 units with an increase of 1% of TMAX. From this table, AWND has a larger effect on Dallas Daily Mean NO2 Concentration.

Next is the table of “Los Angeles Daily Mean PM10 Concentration” and “PRCP, AWND, and TAVG”, from the table, when PRCP increases about 1%, the daily mean PM 10 concentration will decrease by about 1.5219 units. When AWND increases 1%, the daily mean PM 10 concentration will decrease by 4.0278 units. The daily mean PM 10 concentration will increase approximately 39.1553 units with an increase of 1% of TAVG. From this table, TAVG has a larger effect on Los Angeles Daily Mean PM10 Concentration.

The third table is New York “Daily AQI Value PM25” and “PRCP, AWND, and SNWD”. From the table, when PRCP increases about 1%, the PM25 value of AQI will decrease by about 1.1931 units. When AWND increases 1%, the PM25 value of AQI will decrease by about 21.0091 units. The AQI value PM25 will increase approximately 4.8093 units with an increase of 1% of SNWD. From this table, AWND has a larger effect on AQI value PM25 every day in New York. 

The last table is the collection of five cities “Daily AQI Value PM25” and “lag_WT01, PRCP, AWND, SNWD, lag_PM25”. In this whole table, we added one artificial variable called WT01 which includes fog, ice fog, freezing fog, and hoped to consider the lag effect of fog. According to this table, when lag_WT01 increases 1%, AQI value PM25 will decrease 6.0507 units. Similarly, the rise of PRCP and AWND will cause the fall of the PM25 value. The SNWD and lag_PM25 might increase the AQI value of PM25 every day in five cities. 

From the result of the four tables, we can get the conclusion that Precipitation, Average Wind Speed might decrease the value of three pollution indicators, and snow depth might cause the increase of pollution indicators. 

### Limitations:


### Extensions:

The extension of our analysis and our research can be divided into three parts. The first is R-squared from OLS regression tables is too small. Maybe we should consider more variables in the weather data. In addition, maybe more social factors like the price of petrol can also influence the value of air pollution indicators like PM 2.5. The next part is we should consider more integral and specific weather data. In this project, we just used the data from the airport station of each city. However, there are more stations in each city, and we should collect more stations’ data which get the comprehensive weather conditions. Several stations’ data can help us analyze the relationship in this process. The third part is related to our research, and we can do the time series in the future. Although we did the lag_PM2.5, we could investigate how pm2.5 influences the value of pm2.5 in two days, three days. We wanted to investigate the delayed influence of air pollution indicators. Those are three fields that we can do additional work to the analysis and the research. 

## Report on the Data:

We selected 5 areas to collect their daily pollutants and weather, which is Austin, Dallas, Houston, Los Angeles and New York.

### Source(s) of datasets:

The data of daily pollutants:
https://www.epa.gov/outdoor-air-quality-data/download-daily-data
The data of weather:
https://www.weather.gov/wrh/Climate?wfo=fwd

### Data collection methods:


### Limitations of the data:

We choose NO2, pm10 and pm2.5 as daily pollutants, however, there’s still other pollutants that we do not cover, such as CO, SO2, Pb and Ozone.

### Extensions:

If further analysis is required, we can add those pollutants in our codes to get more accurate results. 

