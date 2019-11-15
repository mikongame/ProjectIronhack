# My functions

#### PREPROCESSING FUNCTIONS #####

def percentNulls(df):
    '''
    Detect the columns that have a higher number of nulls
    input= dataframe 
    outut= name of the columns and % of nulls higher of 10%
    '''        
    for col in df.columns:
        if df[col].isnull().sum() > 0:
            ratio = df[col].isnull().sum()/len(df['deviceBrowser'])
            if ratio > 0.1:
                print(f'**{col}** % Nulls is {round(ratio*100,2)}')


#### EDA FUNCTIONS ####
def desc_num(x, bins=100, name='column'):
    import seaborn as sns
    import matplotlib.pyplot as plt
    import math
    '''
    Describe numerical vars and draw histogram and boxplot
    input= dataframe column, num of bins and name of the column
    outut= describe of the column values, histogram and boxplot
    '''
    null = x.isnull().sum()
    print("Numbers of Nulls: ", null)
    descript = x.describe()
    print("The description of this variable is:\n", descript)
    dist = x.hist(bins=bins).set_title(f'Histogram of {name} with bins={bins}')
    plt.show()

    box = sns.boxplot(x=x).set_title(f'Boxplot of {name}')
    plt.show()
    
    
def desc_cat(df,col, name='column'):
    import seaborn as sns
    import matplotlib.pyplot as plt
    import math
    '''
    Describe categorical vars and draw bar chart
    input= dataframe column
    outut= describe of the column values, bar chart
    '''
    null = df[col].isnull().sum()
    print("Numbers of Nulls: ", null)
    values =  df[col].value_counts()
    print(values)
    plt.subplots(figsize=(10, 6))
    bar = df.groupby(col)['fullVisitorId'].count().reset_index()
    bar.columns = [col,'count']
    sns.barplot(x=col, y='count', data=bar)
    plt.title(f'Bar chart {name}')
    plt.xticks(rotation=90)
    plt.show()
    
    
def desc_cat_target(df, col, target, name='column'):
    import seaborn as sns
    import matplotlib.pyplot as plt
    import math
    '''
    Compare the values of the categorical with the target
    input= dataframe column
    outut= column values compared to the target and stacked bar chart column / target
    '''
    df_grouped = df.groupby(col)[target].value_counts().unstack(level=1).fillna(0)
    print(df_grouped)
    df_grouped.plot.bar(stacked=True, figsize=(10, 6))    
    plt.title(f'Stacked Bar chart {name} vs target')
    plt.xticks(rotation=90)
    plt.show()
