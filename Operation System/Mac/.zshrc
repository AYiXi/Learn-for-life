# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
export ZSH="/Users/ayixi/.oh-my-zsh"
alias z="zsh"
alias c="clear"
alias dk="docker"
alias pag="ps -ef | grep"
alias pa="ps -aux"
alias redis="redis-cli"
alias youget="you-get -x 127.0.0.1:1081 -o /Users/ayixi/Downloads"
alias jn="cd /Users/ayixi/Documents/Code/jupyter_notebook;jupyter notebook"
alias vscode="open -a Visual\ Studio\ Code"
alias pycharm="open -a Pycharm"
alias goland="open -a goLand"
alias idea="open -a IntelliJ\ IDEA"
alias studio="open -a Android\ Studio"
alias iterm="open -a iTerm"

alias dc="cd ~/Documents"
alias dn="cd ~/Downloads"
alias code="cd ~/Documents/Code"

alias blog="cd /Users/ayixi/Documents/Code/move_blog_spider"
alias blog_fo="cd /Users/ayixi/Documents/Code/move_blog_spider/move_blog_spider/spiders/foreign_blog"
alias blog_si="cd /Users/ayixi/Documents/Code/move_blog_spider/move_blog_spider/spiders/single"
alias blog_medium="cd /Users/ayixi/Documents/Code/move_blog_spider/move_blog_spider/spiders/medium"
alias blog_wechat_appium="cd /Users/ayixi/Documents/Code/move_blog_spider/move_blog_spider/spiders/wechat_appium"

alias blink="cd /Users/ayixi/Documents/Code/move_blink_spider/move_blink_spider"
alias blink_sites="cd /Users/ayixi/Documents/Code/move_blink_spider/move_blink_spider/sites"
alias blink_weibo="cd /Users/ayixi/Documents/Code/move_blink_spider/move_blink_spider/sites/weibo"
alias blink_douyin="cd /Users/ayixi/Documents/Code/move_blink_spider/move_blink_spider/sites/douyin"

alias video_sites="cd /Users/ayixi/Documents/Code/move_video_spider/move_video_spider/sites"
alias video_bilibili="cd /Users/ayixi/Documents/Code/move_video_spider/move_video_spider/sites/bilibili"
alias video_youtube="cd /Users/ayixi/Documents/Code/move_video_spider/move_video_spider/sites/youtube"

alias anyproxy_js="cd /Users/ayixi/Documents/Code/anyproxy/js"
alias dex2jar="sh /Users/ayixi/Documents/Soft/dex2jar/d2j-dex2jar.sh"

alias mas="git ck master"
alias dev="git ck dev"
alias vsz="vscode ~/.zshrc"
alias sv="source ~/.vimrc"

# homebrew not auto update
export HOMEBREW_NO_AUTO_UPDATE=true

export GO111MODULE=auto
export GOPROXY=https://goproxy.cn
export GOPATH=/Users/ayixi/gopath
export GOBIN=$GOPATH/bin
# export PATH=$PATH:$GOBIN

# export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk-14.0.1.jdk/Contents/Home
export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_144.jdk/Contents/Home
export CLASS_PATH=$JAVA_HOME/lib
export PATH=$JAVA_HOME/bin:$PATH

export HADOOP_HOME=/usr/local/hadoop-3.1.3
export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

export PYTHONPATH2=/Users/ayixi/Documents/Code/move_blog_spider
export PYTHONPATH3=/Users/ayixi/Documents/Code/python/SourceCode
export PYTHONPATH4=/Users/ayixi/Documents/Code/move_video_spider
export PYTHONPATH5=/Users/ayixi/Documents/Code/move_blink_spider
export PYTHONPATH6=/Users/ayixi/Documents/Code/python/Crawler
export PYTHONPATH=$PYTHONPATH2:$PYTHONPATH4:$PYTHONPATH5:$PYTHONPATH6

GRADLE_HOME=/usr/local/Cellar/gradle/6.5
export GRADLE_HOME
export PATH=$PATH:$GRADLE_HOME/bin

export M3_HOME=/usr/local/maven/apache-maven-3.6.3
export PATH=$M3_HOME/bin:$PATH

# export ANDROID_HOME=/usr/local/share/android-sdkb
ANDROID_HOME=/Users/ayixi/Documents/Soft/android-sdk-macosx
export ANDROID_HOME
export PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools

# mongodb
export PATH=/usr/local/mongodb/bin:$PATH

export LANG=en_US.UTF-8
# Set name of the theme to load --- if set to "random", it will
# load a random theme each time oh-my-zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
ZSH_THEME="jonathan"

# Set list of themes to pick from when loading at random
# Setting this variable when ZSH_THEME=random will cause zsh to load
# a theme from this variable instead of looking in $ZSH/themes/
# If set to an empty array, this variable will have no effect.
# ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion.
# Case-sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to automatically update without prompting.
# DISABLE_UPDATE_PROMPT="true"

# Uncomment the following line to change how often to auto-update (in days).
# export UPDATE_ZSH_DAYS=13

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS=true

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# You can set one of the optional three formats:
# "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# or set a custom format using the strftime function format specifications,
# see 'man strftime' for details.
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load?
# Standard plugins can be found in $ZSH/plugins/
# Custom plugins may be added to $ZSH_CUSTOM/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(git)

source $ZSH/oh-my-zsh.sh

# User configuration

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='mvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"
