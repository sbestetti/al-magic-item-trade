cd src
coverage run --source=. -m unittest
coverage html
cp -r /home/sbestetti/apps/al-magic-item-trade/src/htmlcov/ /mnt/d/report/