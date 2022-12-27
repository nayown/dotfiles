#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

PS1='[\u@\h \W]\$ '

# Aliases
alias ls='ls --color=auto'
alias ll='ls -alFs'
alias bsp='vim ~/.config/bspwm/bspwmrc'
alias sxh='vim ~/.config/sxhkd/sxhkdrc'
alias bar='vim ~/.config/polybar/config.ini'
alias barr='source ~/.config/polybar/launch.sh'
alias kit='vim ~/.config/kitty/kitty.conf'
alias vb='vim ~/.bashrc'
alias vbr='source $HOME/.bashrc'
alias vx='vim ~/.xinitrc'
alias vr='vim ~/.vimrc'
alias v='vim'
alias cw='wal -i $HOME/Wallpaper/Hwall && . $HOME/compile.sh'
alias cwh='wal -i $HOME/Wallpaper/Wallhaven && . $HOME/compile.sh'
alias cww='wal -i $HOME/Wallpaper/Wall && . $HOME/compile.sh'
alias b='bat'
alias pac='sudo pacman'
alias pacu='sudo pacman -Syu'
. "$HOME/.cargo/env"
