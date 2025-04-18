# Altium Interactive BOM Releaser

This toolchain enables the generation of [InteractiveHtmlBom](https://github.com/openscopeproject/InteractiveHtmlBom)-compatible HTML files from Altium projects with design variants.
It is composed of three stages:

1. **Altium Output Job**
   Uses a script based on [InteractiveHTMLBOM4Altium2](https://github.com/zharovdv/InteractiveHTMLBOM4Altium2) (we use our [own fork](https://github.com/StefanRickli/InteractiveHTMLBOM4Altium2) for `altium-ibom-releaser`) to export intermediate files:
   - A “Generic JSON” file for the IBOM tool
   - A Pick-and-Place CSV file containing component placement data

2. **Python Patcher**
   A Python tool processes the files above to generate a corrected ["Generic JSON"](https://github.com/openscopeproject/InteractiveHtmlBom/blob/master/InteractiveHtmlBom/ecad/schema/genericjsonpcbdata_v1.schema) file.
   This step patches missing components that are skipped in Altium’s broken scripting API (specifically, when variants are involved).

3. **IBOM Generator**
   The official [InteractiveHtmlBom](https://github.com/openscopeproject/InteractiveHtmlBom) from `KiCad` is used to generate the final self-contained HTML IBOM file from the patched JSON.

---

## 🛠 Why the Intermediate Step?

Due to limitations in Altium’s scripting engine, components defined in design variants **cannot be reliably accessed** via scripts. As a workaround, we use:

- The **Pick-and-Place CSV export**, which correctly reflects variant information
- The **NO_VARIATION JSON**, which is the only reliably complete JSON file

By using the NO_VARIATION output as a base, and merging variant-specific data from the CSV files, we can reconstruct a valid Generic JSON file for each variant.

---

## Usage

Please follow the following steps to include `altium-ibom-releaser` in your Project Release:

### Installation using project script

1. Clone or download the repository to an arbitrary location on your computer.
2. Open a PowerShell terminal
3. `cd <path to the repository>`
4. Run the installation script `.\install.ps1 exe`. This will:
   - Copy the `altium-ibom-releaser.exe` executable to `%USERPROFILE%\bin`
   - Add `%USERPROFILE%\bin` to your `PATH` environment variable (if not already present)
5. Copy following files into the root directory of your Altium project:
   - `InteractiveHTMLBOM4Altium2.pas`
   - `InteractiveHTMLBOM4Altium2.dfm`
6. For your Altium Project:
   - `Right Click on Project > Add Existing to Project > All Files`
     - `InteractiveHTMLBOM4Altium2.pas`
     - `InteractiveHTMLBOM4Altium2.dfm`
   - `Right Click on Project > Add New to Project > Output Job File`
7. In the Output Job:
   - Create the necessary output steps:
     - `Assembly Outputs > Add New Assembly Output > Generates Pick and Place files > [PCB Document]`
     - Enable the Pick and Place step for the `Folder Structure` in the right panel. **It needs to be step 1 in the list.**
     - `Report Outputs > Add New Report Output > Script Output > [InteractiveHTMLBOM4Altium2]`
     - Enable the Script Output step for the `Folder Structure` in the right panel. **It needs to be step 2 in the list.**
   - `Report Outputs > Right Click on the Script > Configure`, and set the parameters according to your project's needs:
   - `Assembly Outputs > Right Click on the Pick & Place Step > Configure`:
     - Select `CSV` as the output format.
     - Separator: `.` (dot)
     - **IMPORTANT:** You need to select at least the same columns as in the script configuration, otherwise, `altium-ibom-releaser` will complain about missing columns in the CSV file.
     - `Include Variation Component` must be **disabled**
   - `Output Containers > Folder Structure > Change`:
     - Set the output folder if you want a different location than `ibom`.
     - `Advanced`:
       - `Open generated outputs`: **disabled**
       - `Add generated files to project`: **disabled**
   - `Generate Content`: This is a test run. If all goes well, you should see the following files in the output folder:
     - `ibom\iBOM for <PcbDoc Name>.cfg`
     - `ibom\iBOM for <PcbDoc Name>.json`
     - `ibom\iBOM for <PcbDoc Name>_patched.json`
     - `ibom\Pick Place for <PcbDoc Name>.csv`
     - `ibom\ibom.html` <-- This is the final output file, which is generated by the `InteractiveHtmlBom` tool.
8. `Right Click on Project > Project Releaser`:
   - Select **all** Assembly Data Variants, also `No Variant`!
   - On the bottom of the window, click `Options`. Under `Assembly Data`, enable `altium-ibom-releaser`.
   - Click `OK` to close the options window.
   - Click `Prepare` to start the project release process.
   - The Pascal script will be executed for each variant during Assembly Data generation. It will call `altium-ibom-releaser` to patch the JSON file and generate the final HTML file using `InteractiveHtmlBom`.
   - Click `View` of the `ibom` entries to inspect the generated files. The final HTML file should be located in `ibom\ibom.html` for each variant.
   - Click `Release` to transfer the files into the actual release.

### Manual installation
1. Download the files from the latest [release](https://github.com/StefanRickli/altium-ibom-releaser/releases) of this repository.
2. Copy the executable into any location of your `PATH` environment variable.
3. Continue at step 5 of the installation using project script.

### Updates

Updates to `altium-ibom-releaser` have two scopes:

- **.pas/.dfm** files: Unfortunately, because we need to add them to each project, each project needs to be updated manually.
- **Executable**: The executable is a standalone file, outside your Altium project. You can simply replace the old version with the new one (using manual overwrite or new invocation of `install.ps1`). The new version will be used in the next project release. That means, updates to the visuals of the HTML file will be automatically included in the next project release.

## Python Package Development

**Prerequisites**: Python 3.10+, and either `python` or `py` in your `PATH` environment variable.

### Installation

1. Clone the repository to an arbitrary location on your computer.
2. Perform the same steps of normal installation using the installation script, but instead of executing `.\install.ps1 exe`, run `.\install.ps1 editable`. The script will now:
   - Setup a virtual environment in the `.venv` folder of the repository
   - Install the dependencies from `requirements.txt` into the virtual environment
   - Install the `altium-ibom-releaser` package into the virtual environment as editable package
   - Install `pre-commit` hooks for basic code and commit message checks
   - Install a shim EXE in `%USERPROFILE%\bin` that will call the virtual environment's Python interpreter and the `altium-ibom-releaser` package
   - Add `%USERPROFILE%\bin` to your `PATH` environment variable (if not already present)

### Version numbers and Commit messages

This project follows [Semantic Versioning](https://semver.org/) and uses [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) for commit messages.
The version number is stored in `src/altium-ibom-releaser/__init__.py` and is automatically updated by the `dev.ps1` script. **The commit message must follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) format, otherwise, the commit will be rejected by the pre-commit hook.**

In short, the commit message must start with one of the following prefixes, see [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) for more details:
- `fix:`: Bug fix (patch version)
- `feat:`: New feature (minor version)
- `feat!:`: New feature with breaking change (major version)
- `build:`: Build system changes (no version change)
- `ci:`: Continuous Integration changes (no version change)
- `docs:`: Documentation changes (no version change)
- `perf:`: Performance improvements (no version change)
- `refactor:`: Code refactoring (no version change)
- `style:`: Code style changes (no version change)
- `test:`: Test changes (no version change)
- `chore:`: Other changes (no version change)

### Development tasks

`dev.ps1` implements a variety of development tasks. Run `.\dev.ps1 help` to see the available options.

### Releasing

`dev.ps1 release` will perform the following steps:
- Increase the version number according to the commit message prefixes present in the latest commits since the last release
- Update the `CHANGELOG.md` file with the latest changes
- Build the Python package into a single self-contained executable using [PyInstaller](https://pyinstaller.readthedocs.io/en/stable/)
- Put the executable into the `release` folder, stage it for a commit
- Commit the changes with a message like `chore(release): vX.Y.Z`
- Tag the commit with the version number
- Push the commit and tag to the remote repository
- A GitHub action will automatically create a new release upon push of the tag

---

## 🔗 Related Projects

- [InteractiveHtmlBom](https://github.com/openscopeproject/InteractiveHtmlBom)
- [InteractiveHTMLBOM4Altium2](https://github.com/zharovdv/InteractiveHTMLBOM4Altium2) (original Altium script)

---

Feel free to suggest improvements or contribute patches!
