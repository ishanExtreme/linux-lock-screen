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

- Create an account at https://pushover.net/
- On the dashboard screen scroll to bottom and click on "Create an Application/API token" and fill necessary details
- Create .env file in the project directory and fill up the following variables: PUSHOVER_TOKEN, PUSHOVER_USER, PUSHOVER_DEVICE

Change configuration file(OPTIONAL):

- You can update config.py to change certain behaviours of the programme

Start the script:

- run start.sh
- To lock press ctrl+k and to unlock press the same button (ctrl+k)

### ✨ Current Features

> 1. Responsive Design to support all devices.
> 2. Board feature to devide tasks into different categories.
> 3. Drag & Drop to change task category
> 4. Kanban-style workflow.

### 🧑‍💻 Tech Stack Used

> 1. Front End: front end is made using **React(TypeScript)** and **Tailwind** and **Framer Motion** for animation.
> 2. Back End: back end is REST based using **Django** with **Django Rest Framework Library** and **Postgresql** for database.
> 3. Cloud Service: **Heroku** for backend and **Netlify** for frontend

### 🚀 Running Locally

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

### 🤝 Contributing

> Contributions, issues and features requests are welcome!

### ⚠️ License

> GNU General Public License v3.0 or later <br/>
> See [COPYING](https://github.com/ishanExtreme/Truth_Dare/blob/master/COPYING.txt) to see the full text.

<h2 align='center'>
  Do star ⭐ the repo if you like the project
</h2>

<!-- 3rd api party used -->
<!-- Twilio for WA -->
<!-- Mailgub for emails -->
