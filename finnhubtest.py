import pandas as pd 
import finnhub as fh
import time
import datetime
import numpy as np
#single function call that uses only 1 API call to gather all information needed for the 7 day gain loss,
#7 day spread, avg volume for 30 days, and volume/avg leading up to earnings.
def get_day_gl(row):
    return_list = []
    volumethirty = 0.0
    volumecount = 30

    #retrieve stock candles for set amount of days (using 40 to account for closed days.)
    data = finnhub_client.stock_candles(row.Symbol, 'D', row.UnixDate-(162000*50), row.UnixDate)
    time.sleep(1)
    # testing - print(data)
    #does this symbol have the associated data? if so carry on.
    if (data['s'] == 'ok' and len(data['c']) >= 7):
        #calculate gain loss using open and close prices.
        for index in range(7):
            return_list.append(float(data["c"][-1-index]) - float(data["o"][-1-index]))
        #calculate 7 day spread using high and low prices.
        for index in range(7):
            return_list.append(float(data["h"][-1-index]) - float(data["l"][-1-index]))

        #calculate avg 30 day volume.
        if (len(data['v']) < 30 ):
            volumecount = len(data['v'])

        for index in range(volumecount):
            if volumecount == 0:
                return retur
            volumethirty += float(data["v"][-1-index])

        return_list.append(volumethirty)

        #percentage of 30 day volume per each day.
        for index in range(7):
            if volumethirty == 0.0:
                return_list.append(0)
            else:
                return_list.append(float(data["v"][-1-index]) / volumethirty)
        
        return return_list
    else:
        return[]

def testfunct(row):
    if type(row.Symbol)==str:
        return pd.Series([len(row.Symbol),len(row.Symbol)*2])
    else:
        print(row.unixdate)
        print(type(row.Symbol))
        return
start_pos = int(input('Enter starting position: ' ))
end_pos = int(input('Enter ending position -1'))
#we have to access the rows from start pos to the final position.
#ymbol = 'AAPL'

finnhub_client = fh.Client(api_key="c007cpn48v6v49v2bat0")
#res = finnhub_client.stock_candles(symbol, 'D', 1591315200-(16200*6), 1591315200)
#print(res)

dataset = pd.read_csv("C:/datasets/Earnings20-05.csv", names = ['EarningsDate', 'Symbol', 'After/Before Market', 'Market_Cap'])

print(dataset.head())
dataset['EarningsDate'] = pd.to_datetime(dataset['EarningsDate'])
dataset['UnixDate'] = dataset.EarningsDate.values.astype(np.int64) // 10 ** 9
print(dataset.head())

dataset[['day1gainloss','day2gainloss','day3gainloss','day4gainloss','day5gainloss','day6gainloss','day7gainloss','day1spread','day2spread','day3spread','day4spread','day5spread','day6spread','day7spread','30dayvolume','day1prop','day2prop','day3prop','day4prop','day5prop','day6prop','day7prop']] = dataset.iloc[start_pos:end_pos].apply((lambda row: pd.Series(get_day_gl(row))), axis =1)
#df.apply(lambda row: pd.Series(add_subtract(row['a'], row['b'])), 
dataset.iloc[start_pos:end_pos].to_csv("C:/datasets/outputfinn.csv", mode = 'a', header = False)

#print(res)
#df = pd.DataFrame(res)

#df['open_close_diff'] = df.apply(lambda row: row.o - row.c, axis = 1)
#print(df)
#df_1 = df.copy()
#df_1 = df_1['open_close_diff']
#plt.hist(df_1, bins=20, orientation='vertical', color=('blue'),edgecolor = 'w', label='Open Close Difference Histogram')
#df_1.hist(bins = (20)

#plt.show()

