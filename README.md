# Altium Interactive BOM Releaser

This app consists of three parts:
1) Altium Output Job (using Script originally from [InteractiveHTMLBOM4Altium2](https://github.com/zharovdv/InteractiveHTMLBOM4Altium2) that exports intermediate files, and calls:
2) A file patcher, written in Python, that uses the information from the various file sources to generate a ["Generic JSON"](https://github.com/openscopeproject/InteractiveHtmlBom/blob/master/InteractiveHtmlBom/ecad/schema/genericjsonpcbdata_v1.schema) file, compatible with the JSON schema of KiCad's plugin [InteractiveHtmlBom](https://github.com/openscopeproject/InteractiveHtmlBom). It calls:
3) InteractiveHtmlBom to generate the self-contained IBOM HTML from the intermediate Generic JSON.

The intermediate files step is needed because the Altium scripting engine is so broken that components, which belong to a design variation, cannot be iterated over using Altium scripts. Exporting the native Pick'n'Place CSV file allows to patch the missing information.

This necessitates to use Altium's Project Releaser. It generates all the variation outputs, including the broken JSONs, but the NO_VARIATION JSON is complete. We use this base file to patch the JSON of the variations.

## Project Development Status
- [x] Correct Python project setup, with development, build, and self-contained EXE generation in mind
- [x] Allow reliable project installation or executable copy into System's PATH, such that it can be used globally in a shell - using a script.
- [ ] Define Output Job which contains:
  - [ ] Integrate rewritten [InteractiveHTMLBOM4Altium2](https://github.com/zharovdv/InteractiveHTMLBOM4Altium2) that only outputs Generic JSON
  - [ ] Definition of Pick and Place CSV export
- [ ] Per Variation in Output Job:
  - [ ] Call file patcher
  - [ ] Convert intermediate Generic JSON to self-contained Interactive HTML BOM
