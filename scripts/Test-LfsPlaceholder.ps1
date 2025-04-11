param (
    [Parameter(Mandatory = $true)]
    [string]$FilePath
)

if (-not (Test-Path -Path $FilePath)) {
    throw "File not found: $FilePath"
}

try {
    $lines = Get-Content -Path $FilePath -TotalCount 3 -Encoding UTF8
} catch {
    throw "Failed to read file: $FilePath"
}

if ($lines.Count -ge 3 -and $lines[0] -eq 'version https://git-lfs.github.com/spec/v1') {
    $oid = ($lines[1] -split ' ')[1]
    $size = ($lines[2] -split ' ')[1]

    Write-Output "🧪 Detected Git LFS placeholder:"
    Write-Output "    ➤ File : $FilePath"
    Write-Output "    ➤ OID  : $oid"
    Write-Output "    ➤ Size : $size bytes"
    Write-Output ""
    Write-Output "💡 To fetch this file:"
    Write-Output "  1. Clone the project with Git LFS: git clone --recursive <repo-url>"
    Write-Output "  2. Or download the real file from the project's website if available."

    throw "File is a Git LFS placeholder."
} else {
    exit 0
}
