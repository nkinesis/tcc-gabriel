cd ..\build_ds
python 1_bs_client.py
python 1_bs_country.py
python 2_prods_by_country.py
python 3_ratings_c_cbr_acf.py
cd ..\predict
python recomm-train.py 3 c_cbr_acf.csv
python recomm-test.py 123 456 c_cbr_acf.csv