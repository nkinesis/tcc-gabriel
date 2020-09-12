cd C:\laragon\www\tcc-gabriel\src\classif\2020_2\recomm\build_ds
python 1_bs_client.py
python 2_bs_country.py
python 3_ratings_c_cbr.py
cd ..
cd C:\laragon\www\tcc-gabriel\src\classif\2020_2\recomm\predict
python recomm-train.py 3 c_cbr.csv
python recomm-test.py 123 456 c_cbr.csv