import pandas as pd 
import matplotlib.pyplot as plt
import finnhub as fh
symbols = ['AAPL', 'GOOG', 'CVS']
finnhub_client = fh.Client(api_key="bu55n6f48v6uemrm3mvg")

def dataframcalc (symbol_list):
    empty_dict = {}
    for symbol, index in symbol_list, range(3):
        
        res = finnhub_client.stock_candles(symbol, 'D',1589068800, 1602932400)
        df = pd.DataFrame(res)
        df['open_close_diff'] = df.apply(lambda row: row.o - row.c, axis = 1)
        plt.hist(df['open_close_diff'], bins=20, orientation='vertical', color=('blue'),edgecolor = 'w', label='Open Close Difference Histogram')

dataframcalc(symbols)
plt.show()






#print(df)
#df_1 = df.copy()
#df_1 = df_1['open_close_diff']
#plt.hist(df_1, bins=20, orientation='vertical', color=('blue'),edgecolor = 'w', label='Open Close Difference Histogram')
#df_1.hist(bins = (20)



