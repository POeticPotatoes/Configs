#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '

dotnetbuilder() 
{
    ~/scripts/cbuilder.sh
}

custominit()
{
    ~/scripts/init.sh
}

shopt -s extglob
export DEBUGINFOD_URLS="https://debuginfod.archlinux.org"
