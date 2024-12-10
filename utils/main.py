from jinja2 import Environment, FileSystemLoader
import os
import typer
from typing_extensions import Annotated
import logging

# Configure the logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
######## Utility functions #########
def render_template(template_path: str, context: dict) -> tuple[str, str]:
    env = Environment(loader=FileSystemLoader(template_path))
    code_template = env.get_template("code_template.j2")
    readme_template = env.get_template("readme_template.j2")
    return code_template.render(context), readme_template.render(context)


def create_folder_if_not_exists(folder_path):
    """
    Create a folder if it does not exist.

    Args:
    - folder_path (str): The path to the folder to create.
    """
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        logger.info(f"Folder {folder_path} already exists.")
    else:
        os.makedirs(folder_path)
        logger.info(f"Folder {folder_path} created.")


def create_file_if_not_exists(file_path, content):
    """
    Create a file if it does not exist.

    Args:
    - file_path (str): The path to the file to create.
    """
    if os.path.exists(file_path) and os.path.isfile(file_path):
        logger.info(f"File {file_path} already exists.")
    else:
        with open(file_path, "w") as f:
            f.write(content)
        logger.info(f"File {file_path} created.")

######## CLI #########
app = typer.Typer()

@app.command(help="Generate the data folders and code files for the given date.")
def create_day(date: Annotated[str, "The date to create the files for in the format YYYYMMDD"]):
    year = date[:4]
    date_id = int(date[-2:])
    date_dir_path = f"./{year}/{date}"
    part_1_path = f"{date_dir_path}/part_1.py"
    part_2_path = f"{date_dir_path}/part_2.py"
    input_path = f"{date_dir_path}/{date}_input.txt"
    input_example_path = f"{date_dir_path}/{date}_input_example.txt"
    readme_path = f"{date_dir_path}/README.md"

    create_folder_if_not_exists(date_dir_path)

    logger.info(f"Creating files for {date}...")
    template_path = os.path.join(os.getcwd(), "utils")
    code_content, readme_content = render_template(template_path, {"year": year, "date_id": date_id, "date": date})

    create_file_if_not_exists(readme_path, readme_content)
    create_file_if_not_exists(part_1_path, code_content)
    create_file_if_not_exists(part_2_path, code_content)
    create_file_if_not_exists(input_path, "")
    create_file_if_not_exists(input_example_path, "")
    logger.info(f"Files created for {date}.")

if __name__ == "__main__":
    app()