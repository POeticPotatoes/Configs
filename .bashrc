custominit() 
{
    ./scripts/init.sh
}

dotnetbuilder() 
{
    ~/scripts/cbuilder.sh
}

brightness()
{
    xrandr --output DP-0 --brightness $1
}

compile()
{
    set -- "${1}" "${@: -1}"
    set -- "${1}" "${2%.cpp}"
    g++ -std=c++17 -Wshadow -Wall -o "${2}.out" "${2}.cpp" -g -fsanitize=address -fsanitize=undefined -D_GLIBCXX_DEBUG
    echo Compiled: ${2}.out
    if [[ "$OS" = *"Darwin"* ]]; then
        echo "Ptweh! What's this, a mac user!?"
        rm -r "${2}.out.dSYM"
    fi
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

runcpp()
{
    set -- "${1%.cpp}"
    set -- "${1%.}"
    compilecpp ${1}
    if [[ "$OS" = *"Darwin"* ]]; then
        echo "Ptweh! What's this, a mac user!?"
        rm -r "${1}.out.dSYM"
    fi
    ./${1}.out
}

compilecpp()
{
    g++ -std=c++17 -Wshadow -Wall -o "${1}.out" "${1}.cpp" -g -fsanitize=address -fsanitize=undefined -D_GLIBCXX_DEBUG
    echo Compiled: ${1}.out
}

compilec()
{
    set -- "${1%.c}"
    set -- "${1%.}"
    gcc ${1}.c -o ${1}.out
    echo Compiled: ${1}.out
}

runc()
{
    compilec ${1}
    ./${1}.out
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
    if [[ "$OS" = *"Darwin"* ]]; then
        echo "Bleaugh! Weird mac syntax..."
        open https://github.com/POeticPotatoes/${1}
        exit
    fi
    xdg-open https://github.com/POeticPotatoes/${1}
    exit
}

solution()
{
    template="#include <bits/stdc++.h>\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n}"
    set -- "${1%.cpp}"
    if [[ "$OS" = *"Darwin"* ]]; then
        # template="#include \"/Users/poeticpotato/Desktop/Work/cpp/bits.h\"\nusing namespace std;\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n}"
        echo "Yo dawg, I saw you using an inferior OS so i fixed your imports."
    fi
    printf "$template" > ${1}.cpp
}

submit()
{
    if [[ "$OS" = *"Linux"* ]]; then
        cowsay "You don't need this submit function."
        return
    fi
    set -- "${1%.cpp}"
    set -- "${1/%/.cpp}"
    cp $1 ~/Desktop/Work/cpp/submissions/${1}
    sed -i '' '1s/#include.*/#include <bits\/stdc++.h>/g' ~/Desktop/Work/cpp/submissions/${1}
}

export OS=`uname`
