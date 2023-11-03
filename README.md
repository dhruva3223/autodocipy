# autodocipy

autodocipy is a Python library used to automatically generate documentation for Python projects. It utilizes a combination of static code analysis and natural language processing to extract information from Python source files and generate markdown documentation.

## How to Use

### Installation

autodocipy can be installed via pip:


pip install autodocipy


### Generating Documentation

To generate documentation for a Python project, use the `autodocipy-doc` command followed by the source directory and output directory:


autodocipy-doc


This will analyze the Python files in the source directory and generate markdown documentation in the output directory. The documentation can then be served using the `autodocipy-offline` command:


autodocipy-offline


This will start an mkdocs server on port 8000, allowing you to view the generated documentation in your web browser.

### Generating README

autodocipy can also generate a README.md file for your project using the `autodocipy-readme` command:


autodocipy-readme


This will analyze the Python files in the source directory and generate a README.md file using the OpenAI GPT-3.5-turbo language model.

## Documentation Generator

The `autodocipy` library provides a class called `AutoDocipy` for generating documentation. Here are the methods available in this class:

### `_init_(self, source_dir, output_dir)`

Initializes the `AutoDocipy` object with the source directory and output directory.

### `should_ignore(self, path)`

Checks if a file should be ignored during the documentation generation process. This includes files like .git and _pycache_.

### `parse_comments(self, file_path)`

Parses string literals from a Python file and extracts code documentation comments.

### `generate_documentation(self)`

The base function that calls `should_ignore`, `parse_comments`, and `create_and_build_mkdocs_project` to generate and configure the documentation for offline use.

### `generate_file_documentation(self, file_name, comments, folder_name)`

Creates offline markdown documentation for each file in the Python source folder.

### `create_and_build_mkdocs_project(self, mkdocs_project_dir)`

Configures the mkdocs project for serving the generated documentation.

### `generate_readme(self)`

Generates an AUTODOCREADME.md file using OpenAI.

## License

autodocipy is released under the MIT License. See [LICENSE](LICENSE) for more details.
