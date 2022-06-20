#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '

# My Aliases
alias ll='ls -alFs'
alias cw='wal -q -i /home/jem/wallpaper/aniwal'
alias cdt='wal -q -i /home/jem/wallpaper/dt'
alias vqt='vim  ~/.config/qtile/config.py'
alias cqt='code ~/.config/qtile/config.py'  
alias vv='vim ~/.vimrc'
alias vb='vim ~/.bashrc'
alias vx='vim ~/.xinitrc' 
alias hc='hollywood'
# Run neofetch
# neofetch
# Run colorscripts
# colorscript random
