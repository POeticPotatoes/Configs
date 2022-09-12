compile()
{
    set -- "${1}" "${@: -1}"
    set -- "${1}" "${2%.cpp}"
    g++ -std=c++17 -Wshadow -Wall -o "${2}.out" "${2}.cpp" -g -fsanitize=address -fsanitize=undefined -D_GLIBCXX_DEBUG
    rm -r "${2}.out.dSYM"
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
    rm -r "${1}.out.dSYM"
}

cowtell()
{
    fortune | cowsay
}

cowread()
{
    cat $1 | cowsay 
}

repo()
{
    open https://github.com/POeticPotatoes/${1}
}

submit()
{
    set -- "${1%.cpp}"
    set -- "${1/%/.cpp}"
    cp $1 ~/Desktop/Work/cpp/submissions/${1}
    sed -i '' '1s/#include.*/#include <bits\/stdc++.h>/g' ~/Desktop/Work/cpp/submissions/${1}
}

solution()
{
    set -- "${1%.cpp}"
    set -- "${1/%/.cpp}"
    printf "#include \"/Users/poeticpotato/Desktop/Work/cpp/bits.h\"\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n}" > ${1}
}
