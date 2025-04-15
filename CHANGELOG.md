# CHANGELOG

<!-- version list -->

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
