$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest
$PSNativeCommandUseErrorActionPreference = $true # might be true by default

Push-Location $PSScriptRoot\..
try {

    .\scripts\_assert_venv.ps1
    .\.venv\Scripts\Activate.ps1

    # From the following documentation:
    # https://python-semantic-release.readthedocs.io/en/latest/commands.html#semantic-release-version
    #
    # Detect the semantically correct next version that should be applied to your
    # project (based on the commit history since the last release).
    #
    # By default:
    #   * Write this new version to the project metadata locations
    #     specified in the configuration file
    #   * Build the project using :ref:`config-build_command`, if specified
    #   * Create a new commit with these locations and any other assets configured
    #     to be included in a release
    #   * Tag this commit according the configured format, with a tag that uniquely
    #     identifies the version being released
    #   * Push the new tag and commit to the remote for the repository
    #   * Create a release (if supported) in the remote VCS for this tag
    #
    # Changelog generation is done identically to the way it is done in :ref:`cmd-changelog`,
    # but this command additionally ensures the updated changelog is included in the release
    # commit that is made.
    semantic-release version --no-vcs-release
} finally {
    Pop-Location
}
