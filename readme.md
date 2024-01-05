# OpusFilter

OpusFilter is a tool for filtering and combining parallel corpora.

## Custom preprocessors and filters

*CharacterPreprocessor* - preprocessor for replacing or removing different characters that appear in sentences to bring them into the same style.

*EngInBctFilter* - filter that removes pair of sentences where the construction "(англ.)" occurs.

## Usage
1. Clone the repository onto your local machine by following command: `git clone https://github.com/broder009/lingvanex-test.git`
2. Create virtual environment by using: `python -m venv venv`
3. Install requirements: `pip install -r requirements.txt`
4. Set up `config.json` cofiguration file
5. Set up your PYTHONPATH by using `pythonpath.sh` script
6. When you set up your `config.json` file run the following `python main.py` command in terminal 