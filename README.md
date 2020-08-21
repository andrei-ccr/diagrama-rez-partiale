# diagrama-rez-partiale

Converts data from CSV files provided by Biroul Electoral Central (https://prezenta.bec.ro) into easier to read pie charts.

## Prerequisites
Must be executed using Python 3. Requires `matplotlib` and `pandas` that can be installed using pip:

`pip install matplotlib pandas`

#### How to use
1. Download a CSV file containing voting data (example: https://prezenta.bec.ro/prezidentiale24112019/romania-pv-part)
2. Execute the script with:

`python rezultate.py -f FISIER_CSV NUME_ALEGERI`

where NUME_ALEGERI can be: `2019euro`, `2019tur1` or `2019tur2` depending on the CSV file. 
