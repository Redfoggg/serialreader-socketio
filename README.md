<h1 align="center"> ✨ Flask + SocketIo with React + Socket-io-client Boilerplate ✨ </h1>

### Introduction

This project is a prototype to be used as source to bigger projects who need a Two-way kind of relation between arduino/micro-controllers
or any information that can be extracted by an serial port and plotting the results on react app interface.


### Dependencies

```
python: "3.8.5+", file: "requirements.txt"
node: "10.19.0+", file: "package.json"
npm: "6.14.4+"
pip: "20.0.2+"

```

### Installation

Install the interface dependencies with npm 

```bash
cd interface
npm i
```

Install flask and virtualenv with venv install the packages on requirements.txt

```bsh
pip install flask virtualenv
```

### Usage

Run the python-socket server
```bash
cd server
python app.py
```

Then run the interface

```bash
cd interface
npm start
```


[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
