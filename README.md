## Ames Housing Data and Kaggle Challenge
---

### Summary

In this project, I used the AMES Housing data to create a linear regression model to predict the sale price of a house in Ames Iowa. Based on my Linear Regression, the model can predict the house's price is within $32,000 on average. Based on my model, the features with the most wight to sale price are overall quality, number of full baths, and kitchen quality.

---

### Problem Statement

I was hired by Zillow to help determine if Ames Iowa is a favorable market for tech expansion. Zillow's factors that could suggest tech growth are:
1) Housing affordability
2) Market "hotness"
3) Demographics & Labor Market
4) Tech availability
5) Livability

I am focusing on housing affordability to help determine if Ames is a favorable market for tech expansion. As Zillow suggests, no matter what a resident's income value is, "tech-dominant markets [like San Francisco or Los Angeles] have become notoriously unaffordable." With this in mind, where may the next Silicon Valley lie? Does Ames, Iowa have the desirable mix of affordable housing and the above listed factors? – which, due to the scope of this project, the four other factors won't be explored in detail.

[Source](https://www.zillow.com/research/tech-expansion-markets-2020-26332/)

---

### Provided Data

For this project, we were provided with two datasets:

- [Training Data](./datasets/train.csv)
- [Testing Data](./datasets/test.csv)

---

### Data Cleaining & EDA

#### Model Features Data Dictionary
|Feature|Type|Description|
|---|---|---|
|overall_qual|int64|Overall material and finish quality|
|year_built|int64|Original construction date|
|year_remod/add|int64|Remodel date (same as construction date if no remodeling or additions)|
|exter_qual|int64|Exterior material quality|
|bsmt_qual|int64|Height of the basement|
|bed_bath_ratio|float64|Ratio of number of bedrooms above basement level and full bathrooms above grade|
|bsmt_cond|int64|General condition of the basement|
|bsmtfin_sf_1|int64|Type 1 (Quality of basement finished area) square feet|
|full_bath|int64|Full bathrooms above grade|
|kitchen_qual|int64|Kitchen quality|
|totrms_abvgrd|int64|Total rooms above grade (does not include bathrooms)|
|garage_cars|float64|Size of garage in car capacity|
|garage_area|float64|Size of garage in square feet|
|garage_qual_cars|float64|Ratio of size of garage in car capacity to size of garage in square feet|
|overall_cond_bed_bath|float64|Overall condition rating and bed bath ratio|
|gr_liv_area|int64|Above grade (ground) living area square feet|


#### Missing Values
Many of the missing values in the training dataset were because an observation did not have the specified feature. For example, the original column, `PoolQC` meaning pool quality contained the most missing values. `Nan` values indicated that a house did not have a pool, as indicated in the data dictionary for all 81 columns. I handled this by converting `PoolQC` into a dummy column named `has_pool` where a non-null value, maps to 1, indicating that a pool exists, and a null value maps to 0, indicating that there is no pool. Following this logical imputation process, along with the original data dictionary, I was able to impute parallel missing values with 0's.

#### Ordinal & Nominal Values
Many of the original columns in the training dataset contained values that were ordinal or nominal strings. To be able to plot these columns against sale price later - and determine correlation strength in model feature selection - I replaced ordinal values with integers using a dictionary replacements.


#### Exploratory Visualizations
After managing null values, I looked at the distribution of numerical columns by plotting boxplots and histograms as well as the correlation of features and sale price by running scatter plots/heatmaps. By identifying features that had a stronger correlation with sale price, I created interaction columns that integrate features that are directly related or depend on one another. For instance, I created a new column `bed_bath_ratio` that finds the ratio of the number of bedrooms to number of bathrooms. These two features are more indicative when integrated because they are expected to be proportional, and therefore, their ratio relationship is more important when estimating price.

---

### Modeling

I establisbed my baseline prediction and found that the R2 score is 0. This means that indicates that the model explains none of the variability of the data. I was curious to see how taking the log of saleprice would affect the model so I added a column where I took the logarithm of the saleprice, that is, `train['saleprice_log'] = np.log(train['saleprice'])`. I set the log of sale price to be my target vector and from that, my RMSE score dropped by $10,000. I instantiated, fit, and train/test/split my model to get a trainig R2 score of 85% and test R2 score of 85%. The R2 scores indicates that 85% of the variability in my data can be explained by the linear model. After predicing `X_train`, I was able to get and RMSE score of $31,987.88. This indicates that, based on my Linear Regression, the model can predict the house's price is within $31,987.88 on avereage.

As part of my Zillow assignment, I had to test three different models: Linear Regression, Ridge, and Lasso and compare R2. I used `StandardScalar()` to standardize my data. Standardizing and then fitting `X_train` learns the means and standard deviations of each of our features. Then fit and transform `X_train` and call that `Z_train` to distinguish z-scores. After transforming my features, I instantiated and fit the Ridge and Lasso models, and found that they produce the same R2 scores, meaning they also explain 85% of the variability in the data.

---

### Business Recommendations
Although the Linear Model is not perfect and improving it is an iterative process, it performed well enough to predicted the house's price within $31,987.88 on average. Sale price in Ames, Iowa is, on average, much lower than tech-dominant markets such as Los Angeles or San Francisco. Based on the provided data and Zillow's estimator, [SF Median Home Value](https://www.zillow.com/san-francisco-ca/home-values/) and [LA Median Home Value](https://www.zillow.com/los-angeles-ca/home-values/), I found that in each city, the median sale price values for a home are:
- Ames: $180,500
- Los Angeles: $717,583
- San Francisco: $1,387,263

Given the sale price trends and predictions, Ames, Iowa marks off the housing affordability factor – from which a tech company would benefit expanding to. Affordable housing appeals to outside talent and retains current talent. Although housing in Ames is within a dream price range for an expanding tech market, the other 4 factors must surely be investigated further.

Tech-Available Markets Factor: I researched the [U.S. Bureau of Labor Statistics](https://data.bls.gov/lausmap/showMap.jsp;jsessionid=26AFE327E0F12840099BEBC18A61C7FF._t3_06v) database and found that Ames unemployment rates were at 1.6% in 2018, compared to those in Los Angeles, which were at 4.2%. Zillow states that a labor market with lower unemployment rates can support a growing economy because it leaves room for outside tech talent to come in and take advantage of the unique work-in-tech-own-a-house opportunity.

---

### Sources

- [Zillow Market Expansion](https://www.zillow.com/research/tech-expansion-markets-2020-26332/)

- [U.S. Bureau of Labor Statistics](https://data.bls.gov/lausmap/showMap.jsp;jsessionid=26AFE327E0F12840099BEBC18A61C7FF._t3_06v)

- [U.S. Census, American Community Survey](https://data.census.gov/cedsci/table?q=S1502&table=S1502&tid=ACSST1Y2018.S1502&lastDisplayedRow=24&g=0500000US19169&vintage=2018&mode=)
