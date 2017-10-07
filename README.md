# BitCoin Analysis
This script uses fractal analysis techniques to understand better the way that the BitCoin value changes through time.

##Description

### Time
It only uses data from one year (June, 2016 to June, 2017), but you can download the same data from [this site](https://www.coindesk.com/price/), from any time range you want. I took only one year because it values from before is too low.

### Files

#### analiseRS.py

This is where the core algorithm is put to action.

#### get_data.pl

This script takes the raw data from the csv and formats it so that the Python script can process it.

#### bitcoin_history.txt and coindesk-bpi-USD-close_data-2016-10-06_2017-10-06.csv

The original data. They are the same file, only different formats.

#### btcHistory.txt

The formatted data with only the BitCoin values, not it's date.
