C="/c/Program Files/Google/Chrome/Application/chrome.exe"
W=${1:-430}; H=${2:-6000}; O=${3:-shot.png}
"$C" --headless --disable-gpu --hide-scrollbars --window-size=$W,$H --screenshot="$(cygpath -w "$PWD/$O")" "file:///$(cygpath -m "$PWD/index.html")" >/dev/null 2>&1
