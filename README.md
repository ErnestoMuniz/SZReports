# SZReports
A TelegramReports module for SmartZap reports

## Instalation
First you will need to download or clone this repository and put it on the modules folder.
Then edit the following files:

P.S. The user you will put on the keys must be a manager user.

keys.json
```json
{
  "sz_cookies": "DO NOT MODIFY THIS KEY VALUE",
  "user": "your@email.com",
  "password": "yourpassword"
}
```
variables.json
```json
{
  "url": "https://myexampleurl.sz.chat/",
  "arg": "DO NOT MODIFY THIS KEY VALUE",
  "report": "DO NOT MODIFY THIS KEY VALUE"}
```

model.txt
```text
That's some example text
 - You can put some {keywords} on it -
 \ if you want it to have dinamic data from the API /

 Eg.
    The current time is {time}

 It will be displayed as:
    The current time is 03:46 (or whatever time it is when you give the command)
```


## KeyWords List
KeyWords for model.txt
```python
{day} = Returns the current day of the month
{month} = Return the current month number
{month_name} = Returns the month name
{time} = Returns the current time in the format HH:MM
{waiting} = Returns the amount of the waiting customers
{attendance} = Returns the amount of the in attendance customers
{navigating} = Returns the amount of navigating customers
```

## Usage
First of all, you will need to execute the command `/reload`, this will login your user into the system and give the module the needed authorization credentials.
You will need to run this command whenever you see the informations you need are out of date, it happens because SmartZap automatically logs you out once in a while.


Then you just need to send the following command to receive your report:
```
/sz
```

And you're done! The bot will reply with all the data you wanted.
