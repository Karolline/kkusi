#!/bin/bash
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc

pyenv activate env
python manage.py collectstatic
pip install -r requirements.txt

sudo systemctl daemon-reload
sudo systemctl restart nginx uwsgi
