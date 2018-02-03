# consorsbank - scrape your account page
You have and account with https://www.consorsbank.de/ and wanted to pull information from it.
Until now you where out of luck. The wait is over.
This image lets you get the total balance of your account.

## Usage
In order to get the balance just run the following.

```bash
> docker run -e username=<ACCOUNT_NUMBER> -e password=<ACCOUNT_PW> kairichard/consorsbank
> {"total": "1234.56"}
```
The output is in json for a better composabillity with other tools.

## Contributing Code

If you want to contribute code, please try to:

* Follow the same coding style as used in the project. Pay attention to the
  usage of tabs, spaces, newlines and brackets. Try to copy the aesthetics the
  best you can.
* Write [good commit messages](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html),
  explain what your patch does, and why it is needed.

License
--------
BSD 3
