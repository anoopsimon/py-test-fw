# Test Framework

### Install Dependencies - Windows

1. Create Virtual Environment & Activate: `python -m venv venv && .\venv\Scripts\activate`
2. Install Dependencies : `pip install -r requirements.txt`
3. Run tests : `pytest tests/test.py`
4. deactivate Virtual Environment `deactivate`


### Build in Project in Docker

Build Image : `docker build -t my-selenium-tests .`

Run Container : `docker run -it --rm my-selenium-tests`
