# advent_of_code_practice
Link https://adventofcode.com/

## Configure poetry to use in-project virtual environment
```
poetry config virtualenvs.in-project true
```

## Install the environment
```
poetry install
```

## Run a script
```
❯ poetry run python 2024/20241211/part_2.py
264350935776416
Time taken: 0.03849601745605469 seconds
```

## How-to with the `utils` CLI
Run the following command to generate the date folder and template files
```
❯ poetry runutils 20241211
2024-12-10 10:44:34,177 - INFO - Folder ./2024/20241211 created.
2024-12-10 10:44:34,177 - INFO - Creating files for 20241211...
2024-12-10 10:44:34,178 - INFO - File ./2024/20241211/README.md created.
2024-12-10 10:44:34,178 - INFO - File ./2024/20241211/part_1.py created.
2024-12-10 10:44:34,179 - INFO - File ./2024/20241211/part_2.py created.
2024-12-10 10:44:34,179 - INFO - File ./2024/20241211/20241211_input.txt created.
2024-12-10 10:44:34,179 - INFO - File ./2024/20241211/20241211_input_example.txt created.
2024-12-10 10:44:34,179 - INFO - Files created for 20241211.
```
