# Altium Interactive BOM Releaser

This toolchain enables the generation of [InteractiveHtmlBom](https://github.com/openscopeproject/InteractiveHtmlBom)-compatible HTML files from Altium projects with design variants.
It is composed of three stages:

1. **Altium Output Job**
   Uses a script based on [InteractiveHTMLBOM4Altium2](https://github.com/zharovdv/InteractiveHTMLBOM4Altium2) to export intermediate files:
   - A “Generic JSON” file for the IBOM tool
   - A Pick-and-Place CSV file containing component placement data

2. **Python Patcher**
   A Python tool processes the files above to generate a corrected ["Generic JSON"](https://github.com/openscopeproject/InteractiveHtmlBom/blob/master/InteractiveHtmlBom/ecad/schema/genericjsonpcbdata_v1.schema) file.
   This step patches missing components that are skipped in Altium’s broken scripting API (specifically, when variants are involved).

3. **IBOM Generator**
   The official [InteractiveHtmlBom](https://github.com/openscopeproject/InteractiveHtmlBom) is used to generate the final self-contained HTML IBOM file from the patched JSON.

---

## 🛠 Why the Intermediate Step?

Due to limitations in Altium’s scripting engine, components defined in design variants **cannot be reliably accessed** via scripts. As a workaround, we use:

- The **Pick-and-Place CSV export**, which correctly reflects variant information
- The **NO_VARIATION JSON**, which is the only reliably complete JSON file

By using the NO_VARIATION output as a base, and merging variant-specific data from the CSV files, we can reconstruct a valid Generic JSON file for each variant.

---

## 🚧 Project Status

- ✅ Clean Python project setup:
  - Development and editable installs
  - Build pipeline for generating a self-contained Windows `.exe`
- ✅ Support for global CLI usage (via PATH integration or executable copy)
- ⏳ Output Job Definition:
  - ☐ Integrate a simplified version of [InteractiveHTMLBOM4Altium2](https://github.com/zharovdv/InteractiveHTMLBOM4Altium2) to only export Generic JSON
  - ☐ Include proper Pick-and-Place CSV export definition
- ⏳ Per Variant Processing:
  - ☐ Patch files using the Python tool
  - ☐ Generate self-contained Interactive HTML BOM

---

## 🔗 Related Projects

- [InteractiveHtmlBom](https://github.com/openscopeproject/InteractiveHtmlBom)
- [InteractiveHTMLBOM4Altium2](https://github.com/zharovdv/InteractiveHTMLBOM4Altium2) (original Altium script)

---

Feel free to suggest improvements or contribute patches!
