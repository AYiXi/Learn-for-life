#/bin/bash
chmod +x zsh_install_cn.sh
./zsh_install_cn.sh
cd ~/.oh-my-zsh
git remote set-url origin https://gitee.com/mirrors/oh-my-zsh.git
git pull
git clone https://gitee.com/lxgyChen/zsh-autosuggestions.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions