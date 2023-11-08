<h1 align="center">
  Extreme Linux Lockscreen
</h1>

<h3 align="center">
  Screen lock and mobile notification when someone touches your pc
</h3>
<p align="center">
<a>
    <img style="width:200px" src="./images/logo.png"/>
</a>
</p>
<br/>
<br/>

### 💡 Idea

Imagine you want to monitor something, a long running progress and you don't want anyone to touch your pc during that time. You can use this tool for this, it disables all keyboard and mouse input and also sends a push notification to your mobile phone when someone repeteadely tries to touch your pc.

### 🤔 How To Start Using??

Clone the repo:

```
git clone https://github.com/ishanExtreme/linux-lock-screen.git
```

Install all the requirements:

```
pip install -r requirements.txt
```

Install xtrlock

```
sudo apt install xtrlock
```

Setup push notifications(OPTIONAL)

- Download pushover app from playstore
- Create an account at https://pushover.net/
- On the dashboard screen scroll to bottom and click on "Create an Application/API token" and fill necessary details
- Create .env file in the project directory and fill up the following variables: PUSHOVER_TOKEN, PUSHOVER_USER, PUSHOVER_DEVICE

Change configuration file(OPTIONAL):

- You can update config.py to change certain behaviours of the programme

Start the script:

- run start.sh
- To lock press ctrl+k and to unlock press the same button (ctrl+k)

### ✨ Current Features

> 1. Transparent Lockscreen
> 2. Disables keyboard and mouse input
> 3. Sends notification on too many disturbance to user's mobile

### 🤝 Contributing

> Contributions, issues and features requests are welcome!

### Credits

xtrlock

<h2 align='center'>
  Do star ⭐ the repo if you like the project
</h2>

<!-- 3rd api party used -->
<!-- Twilio for WA -->
<!-- Mailgub for emails -->
