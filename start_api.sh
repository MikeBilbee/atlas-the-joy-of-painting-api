#!/usr/bin/env bash

sudo apt update
sudo apt upgrade
sudo apt install python3-pip
npm install
pip install -r requirements.txt
python3 modify.py 
python3 create_db.py
uvicorn app:app --reload
