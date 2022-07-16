import Nseindia

nse = Nseindia.NSE()

#print(nse.pre_market_categories)
#print(len(nse.pre_market_data('Securities in F&O')))
#print(nse.equity_market_categories)
#print(nse.equity_market_data('NIFTY 50'))
#print(nse.about_holidays())
#print(nse.equity_info('TITAN'))
#print(nse.future_data('ACC', indices=False))
print(nse.option_data('NIFTY', indices=True).to_string())