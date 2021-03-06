# 🚀 Steam hour booster

Python application to increase your time in Steam games, also supports multiple accounts at the same time.

## 🖼 Preview
![Preview](https://i.imgur.com/C3ztAzr.png)

## ⚙ Configuration

In the config.json file you need to enter the username and password of the accounts that need to be boost.

You can find App ID here: [SteamDB](https://steamdb.info)

Usage with Docker is shown below. Fill in config.json file and mount folder with `users_data` to Docker container.
It can also work without Docker in the command line. Just install Python 3 and dependencies.
```
docker build -t hour-booster ./

docker run -d --name boost -v /home/steam-hour-booster/users_data:/home/users_data hour-booster
```

To enter a working container:

```
docker exec -ti boost bash
```
