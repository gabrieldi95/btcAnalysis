# BitCoin Analysis
This script uses fractal analysis techniques to understand better the way that the BitCoin value changes through time.

## Description

This script calculates the [Hurst Exponent](https://en.wikipedia.org/wiki/Hurst_exponent) for a set of values. 

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

### How to use

If you wanna use the same data as this repository, just download everything and run analiseRS.py. If you wanna use a wider range of BitCoin values, download it through this [site](https://www.coindesk.com/price/), then use get_data.pl to get the data ready for the Python script. You can use any set of values, as long as it's in the same format.
