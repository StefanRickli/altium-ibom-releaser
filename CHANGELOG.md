# CHANGELOG

<!-- version list -->

## v0.9.0 (2025-04-16)

### Features

- Add date info to respective field
  ([`5353d9d`](https://github.com/StefanRickli/altium-ibom-releaser/commit/5353d9d40612d949a85e11dac70817c0a714d50f))


## v0.8.0 (2025-04-16)

### Chores

- **version**: Remove constraint to keep major version on zero
  ([`27698db`](https://github.com/StefanRickli/altium-ibom-releaser/commit/27698dbd3aedcfb9de7c0feb6669d86b4a99b2c9))

### Code Style

- Remove debug string
  ([`312b807`](https://github.com/StefanRickli/altium-ibom-releaser/commit/312b80758b8f7a363c6fb41f66a10c6285e34f1f))

### Features

- **config**: Use cfg file to display only the selected columns
  ([`75669cb`](https://github.com/StefanRickli/altium-ibom-releaser/commit/75669cb7caea7c6043f7e9be485c3765c6e2d0f8))

- **directories**: Improve logic to find input files
  ([`7299823`](https://github.com/StefanRickli/altium-ibom-releaser/commit/7299823611099628b04d5cafe5e47778e0424b8a))


## v0.7.1 (2025-04-16)

### Bug Fixes

- **form**: Add missing label definition
  ([`04914e0`](https://github.com/StefanRickli/altium-ibom-releaser/commit/04914e00752b4a079de457b8562dc49fdb9dba0c))

### Chores

- **pre-commit**: Make pushes a bit faster
  ([`cd83fa3`](https://github.com/StefanRickli/altium-ibom-releaser/commit/cd83fa317557afedc6b9421c4a3c3613ff3f33b6))


## v0.7.0 (2025-04-16)

### Bug Fixes

- **fonts**: Let InteractiveHtmlBom handle the components' texts
  ([`f4fb1cf`](https://github.com/StefanRickli/altium-ibom-releaser/commit/f4fb1cf5f82754e81e32213761ace614c51d7262))

### Chores

- **build**: Somehow, __init__.py was not added
  ([`efdd2d1`](https://github.com/StefanRickli/altium-ibom-releaser/commit/efdd2d1e6ca1bcea04ae9af4751760e27ed69789))

### Features

- **ibom4altium**: Merge latest updates from upstream
  ([`974a061`](https://github.com/StefanRickli/altium-ibom-releaser/commit/974a061d0692528909832f529406293d2afcb779))


## v0.6.1 (2025-04-15)

### Bug Fixes

- **ibom4altium**: Predictoutputfilenames crashed upon Project Release preparation start
  ([`29a0eb9`](https://github.com/StefanRickli/altium-ibom-releaser/commit/29a0eb9d54ac41330691545588dc76759250caec))

Because during this invocation, GetBoard has no access to the PcbDoc.


## v0.6.0 (2025-04-15)

### Build System

- **dependencies**: Add colorlog dependency
  ([`cb56e0c`](https://github.com/StefanRickli/altium-ibom-releaser/commit/cb56e0c349a30425d47c5357af78e816e4fb7df4))

- **dev**: Make shim a real executable
  ([`3ac69f9`](https://github.com/StefanRickli/altium-ibom-releaser/commit/3ac69f93e71f8fb1e673ad21617211d3a56fcc72))

Altium must have a complete file name with executable in RunApplication, thus, we cannot use a .bat
  shim

### Features

- Make application fit for Project Releaser
  ([`eff1ad8`](https://github.com/StefanRickli/altium-ibom-releaser/commit/eff1ad89110b85129a428d985f9cad9c9bf6e6a2))

- **app**: Call InteractiveHtmlBom from main to generate final output
  ([`12add8c`](https://github.com/StefanRickli/altium-ibom-releaser/commit/12add8cccf4f30688d334dc2041d4e931c5016e7))


## v0.5.3 (2025-04-15)

### Bug Fixes

- **ci**: Enable Git LFS support for the binary artifact
  ([`5960317`](https://github.com/StefanRickli/altium-ibom-releaser/commit/59603177bc9f4975cb71c957fbe1925a0622ef52))


## v0.5.2 (2025-04-15)

### Bug Fixes

- **ci**: Github_token did not have required permissions
  ([`daf7311`](https://github.com/StefanRickli/altium-ibom-releaser/commit/daf73110b8b9a26f036d81130915622e0cd136e4))

See https://docs.github.com/en/rest/releases/releases?apiVersion=2022-11-28#create-a-release
  https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication#permissions-for-the-github_token


## v0.5.1 (2025-04-15)

### Bug Fixes

- **ci**: Release definition had a filename typo
  ([`987ef19`](https://github.com/StefanRickli/altium-ibom-releaser/commit/987ef19f96173b15b1c64a7edfd1bdd613f776ec))


## v0.5.0 (2025-04-15)

### Bug Fixes

- **install**: Get-systempythonpath was called incorrectly, update docs
  ([`c554474`](https://github.com/StefanRickli/altium-ibom-releaser/commit/c5544742aedf6af7b3887ccec08918f91b89c8ae))

### Build System

- Only copy to release folder when --stage flag is set
  ([`00527fe`](https://github.com/StefanRickli/altium-ibom-releaser/commit/00527fe9ff80eb204df8277102fb3006469fd79a))

### Chores

- **devtools**: Add build command
  ([`e0b48b6`](https://github.com/StefanRickli/altium-ibom-releaser/commit/e0b48b6b7523f54449db05c1b86780b103857945))

- **install**: Add command to install exe or editable python project
  ([`e53cba4`](https://github.com/StefanRickli/altium-ibom-releaser/commit/e53cba4a7131825adb4472cca4d1f27c3646076b))

- **setup**: Make pip install work even with WinPython
  ([`fe47eeb`](https://github.com/StefanRickli/altium-ibom-releaser/commit/fe47eeb884f068c4c24462ccd3e3c9d77040d8a0))

### Continuous Integration

- Add release.yml
  ([`755fd43`](https://github.com/StefanRickli/altium-ibom-releaser/commit/755fd4343be67d6356fd583343af220baa20df4e))

### Documentation

- Add README.md
  ([`04ae160`](https://github.com/StefanRickli/altium-ibom-releaser/commit/04ae160cf5267893e35e1a4dc28562da0b0a94af))

- Fancify README
  ([`b9edad5`](https://github.com/StefanRickli/altium-ibom-releaser/commit/b9edad51b535d5d2d06b6f300289da21be8ebf72))

- **install**: Improve self-documentation
  ([`0cad961`](https://github.com/StefanRickli/altium-ibom-releaser/commit/0cad961a6475c573aedc962aa4cae1a0c25762ce))

### Features

- **ibom4altium**: Switch to refactor branch
  ([`2a9fc8c`](https://github.com/StefanRickli/altium-ibom-releaser/commit/2a9fc8cdc3ec2197e1fab84e85f8fb5277b01b59))

- **main**: Make program a proper cli command
  ([`4affab6`](https://github.com/StefanRickli/altium-ibom-releaser/commit/4affab64c1e6d42b25463e420f2345c6eed8b443))

- **patcher**: Add original patcher PoC
  ([`af19905`](https://github.com/StefanRickli/altium-ibom-releaser/commit/af19905a0096463b467ea76b76b88ea37bf366e2))

- **repo**: Add InteractiveHTMLBOM4Altium2 as submodule
  ([`f1c4728`](https://github.com/StefanRickli/altium-ibom-releaser/commit/f1c472857f93cf2bbf36d61540a284e7dec50675))


## v0.4.0 (2025-04-11)

### Chores

- **scripts**: Make most scripts a command of dev.ps1
  ([`6a30076`](https://github.com/StefanRickli/altium-ibom-releaser/commit/6a30076493ae8f8452e9904c5736774bb0affeb8))

### Features

- **deps**: Update dependencies
  ([`7fc00d2`](https://github.com/StefanRickli/altium-ibom-releaser/commit/7fc00d2b8d436324be37c335dcf8cb93c43ed367))


## v0.3.1 (2025-04-11)

### Bug Fixes

- **build**: Try suppressing git warning `unable to access '\/.config/git/attributes'`
  ([`3e29f70`](https://github.com/StefanRickli/altium-ibom-releaser/commit/3e29f70a904131ed8e8ec141283cc9295cf3aa65))


## v0.3.0 (2025-04-11)

### Bug Fixes

- **build**: Add missing file
  ([`a4abd91`](https://github.com/StefanRickli/altium-ibom-releaser/commit/a4abd91d8c8b35e0578126fe8d94214c3c873643))

### Features

- **build**: Bake version info into executable
  ([`e5e509e`](https://github.com/StefanRickli/altium-ibom-releaser/commit/e5e509e14005c44100b2e01ed35c62e10c7fe8a0))


## v0.2.2 (2025-04-11)

### Bug Fixes

- **release**: Disable GitHub release, add built executable to release folder
  ([`c2da9cf`](https://github.com/StefanRickli/altium-ibom-releaser/commit/c2da9cfd2f75862c488412a379485f11cd98807b))

### Chores

- Add 0.2.1 executable
  ([`d662b6f`](https://github.com/StefanRickli/altium-ibom-releaser/commit/d662b6f3a03db1d67b92814da2d4a79fcde1bee0))

- **git**: Enable Git LFS for executables
  ([`cde6f3c`](https://github.com/StefanRickli/altium-ibom-releaser/commit/cde6f3c6f5ca86d438782d0ab0d30230d6911818))


## v0.2.1 (2025-04-11)

### Bug Fixes

- **semantic-release**: Assume that SSH keys are correctly set up
  ([`7ccfd57`](https://github.com/StefanRickli/altium-ibom-releaser/commit/7ccfd57f16d9c74762d474189164f32b48e7cf6a))

### Chores

- Disable release to VCS
  ([`ab93f48`](https://github.com/StefanRickli/altium-ibom-releaser/commit/ab93f48804aa0eb78838022585ad2759bcd6e74f))

Because the python world has a hard time handling firewalls performing TLS decryption.

- Use release folder for binary location
  ([`0bee4b7`](https://github.com/StefanRickli/altium-ibom-releaser/commit/0bee4b7eba689b7da9818b541618bd6581219f7a))


## v0.2.0 (2025-04-11)

### Chores

- **help**: Hint at generate_interactive_bom command
  ([`09cb45d`](https://github.com/StefanRickli/altium-ibom-releaser/commit/09cb45dae668f02f92f8181dea39e7cc1f8ad87c))

- **help**: Show info about conventional commits when creating new virtualenv
  ([`3039bd7`](https://github.com/StefanRickli/altium-ibom-releaser/commit/3039bd701352582079a4f4f6c356e16e140c8921))

### Features

- **build**: Add working binary releaser
  ([`221922e`](https://github.com/StefanRickli/altium-ibom-releaser/commit/221922efe9198da781c5e2f27c1ce85c728791cb))


## v0.1.0 (2025-04-10)

- Initial Release
