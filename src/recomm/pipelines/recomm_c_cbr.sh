cd ../build_ds
python 1_bs_client.py
python 2_bs_country.py
python 3_ratings_c_cbr.py
cd ../predict
python recomm-train.py 3 c_cbr.csv
python recomm-test.py 123 456 c_cbr.csv
date