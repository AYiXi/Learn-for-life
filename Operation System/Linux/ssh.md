## SSH Settings[The following operations are in sequence]
- on server: `ssh-keygen [-t rsa]` 
- [ssh-copy-id]
  - `cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys`
  - on client: `ssh-keygen`
  - paste windows public key to `~/.ssh/authorized_keys`
  - client config file
- on server: `ssh-keygen`
- `cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys`
- on client: `ssh-keygen`
- paste windows public key to `~/.ssh/authorized_keys`
- client config file
- ssh-copy-id bowang@117.50.135.51
```
Host myali
  HostName 39.105.37.123
  User root
Host xiqing
  HostName 39.105.72.96
  User root
```
[reference](https://www.ruanyifeng.com/blog/2011/12/ssh_remote_login.html)

---

## restart
- systemctl restart sshd

```sh
# 删除之前的信息 
ssh-keygen -R 39.105.37.123
```