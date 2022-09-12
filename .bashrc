custominit() 
{
    ./scripts/init.sh
}

compile()
{
    set -- "${1}" "${@: -1}"
    set -- "${1}" "${2%.cpp}"
    g++ -std=c++17 -Wshadow -Wall -o "${2}.out" "${2}.cpp" -g -fsanitize=address -fsanitize=undefined -D_GLIBCXX_DEBUG
    if [ os == "Mac" ]; then
        echo "Ptweh! What's this, a mac user!?"
        rm -r "${2}.out.dSYM"
    fi
    echo Compiled: ${2}.out
    while getopts ":a" opt; do
      case $opt in
        a)
          ./${2}.out
          ;;
        \?)
          echo "Invalid option: -$OPTARG" >&2
          ;;
      esac
    done
}

fast()
{
    set -- "${1%.cpp}"
    g++ -std=c++17 -Wshadow -Wall -o "${1}.out" "${1}.cpp"
    if [ os == "Mac" ]; then
        echo "Ptweh! What's this, a mac user!?"
        rm -r "${2}.out.dSYM"
    fi
}

cowtel()
{
    fortune | cowsay
}

cowread()
{
    cat $1 | cowsay 
}

repo()
{
    if [ os == "Mac" ]; then
        echo "Bleaugh! Weird mac syntax..."
        open https://github.com/POeticPotatoes${1}
        return
    fi
    xdg-open https://github.com/POeticPotatoes/${1}
}

solution()
{
    set -- "${1%.cpp}"
    printf "#include <bits/stdc++.h>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n}" > ${1}.cpp
}

os()
{
    STR=$(hostnamectl)
    if [[ "$STR" == *"Linux"* ]]; then
        echo "Linux"
        return
    fi
    echo "Mac"
}
