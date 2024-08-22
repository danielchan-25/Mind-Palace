# Q&A
- 每次执行 `git pull` 都需要输入账号密码怎么办?
  
  执行以下命令：
  ```shell
  git config --global credential.helper store  # 配置 Git 凭证存储的命令
  git config --global user.name "username"
  git config --global user.password "password"
  ```
