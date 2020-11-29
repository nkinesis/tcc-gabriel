cd ..\build_ds
python 1_bs_client.py
python 1_bs_general.py
python 3_ratings_g_cbr.py
cd ..\predict
python recomm-train.py 3 g_cbr.csv
python recomm-test.py 123 456 g_cbr.csv