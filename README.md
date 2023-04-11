Python script to capture whole [bancho.py](https://github.com/osuAkatsuki/bancho.py/tree/fdd08ceee4ecd3e0cc2e5ca65ef832156a680870) servers leaderboard everyday on specified time using cron.

#### Setup instructions

```bash
# Copy .env file.
cp .env.example .env

# Fill MySQL data on .env file.
nano .env

# Install pipenv module.
python3.9 -m pip install pipenv

# Add the table to MySQL database.
mysql -u USER -p DATABASE_NAME < base.sql

# Create virtual environment.
PIPENV_VENV_IN_PROJECT=1 pipenv install
```

And, the last thing to do is configure crontab. I use **02:30 AM** of server time to execute the script, but you could configure that easily to any other time you want to just using that [website](https://crontab.guru/).

### Configure cron

```bash
crontab -e

# After a simple config setup of crontab - add the following line.
30 2 * * * /absolute/path/.venv/bin/python /absolute/path/main.py
```