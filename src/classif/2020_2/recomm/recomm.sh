cd build_ds
#python 1_bs_client.py
#python 2_bs_country.py
#python 3_ratings.py
cd ..
cd predict
python recomm-train.py 3
python recomm-test.py 123 456