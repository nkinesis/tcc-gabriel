tcc-activate
cd build_ds
python 1_bs_client.py
python 2_bs_country.py
python 3_ratings.py
cd ..
cd predict
python recomm_train.py 3
python recomm_test.py 123 456