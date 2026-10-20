If necessary: 
python -m pip uninstall -y orbichord

git clone https://github.com/orbichord/orbichord.git
mv orbichord orbichord-source
In requirements.txt, replace pygame with pygame-ce

brew install portaudio

pip install --upgrade pip setuptools wheel pbr
pip install -r requirements.txt
python -m pip install ./orbichord-source

If necessary: 
python -m pip install -e ./orbichord-source