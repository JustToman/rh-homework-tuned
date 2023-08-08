# Red Hat Interview Homework - Paragraph Shuffler

Paragraph Shuffler is a python3 script that accepts input file and pseudo randomly shuffles its paragraphs. The shuffled text is then printed to STDOUT.

## Installation

1. Install [python3](https://www.python.org/downloads/) interpreter (If you don't already have it)
2. Clone this repository
```bash
git clone https://github.com/JustToman/rh-homework-tuned.git
```
3. Enter cloned repository
```bash
cd rh-homework-tuned
``` 


## Usage
Inside the cloned repository you can run the script this way, *<filepath>* is going to be a path to a file where your text with paragraphs to be shuffled is stored.

```bash
python3 script.py --file <filepath>
```


You can also execute the script this way as an executable. But in order to do this you'll need to make the script executable:
```bash
chmod +x script.py
```
and then run it:
```bash
./script.py --file <filepath>
```

## Example
Let's say we have created file inside the cloned repository named input.txt with this contents(Free Software Song, by Richard Stallman):

*Join us now and share the software;
You'll be free, hackers, you'll be free
Join us now and share the software;
You'll be free, hackers, you'll be free*

*Hoarders can get piles of money
That is true, hackers, that is true
But they cannot help their neighbors;
That's not good, hackers, that's not good*

*When we have enough free software
At our call, hackers, at our call
We'll kick out those dirty licenses
Ever more, hackers, ever more*

Now we execute the script like this:
```bash
python3 script.py --file input.txt
```
The output could look like this (it won't always be the same since it's pseudo random):

*When we have enough free software
At our call, hackers, at our call
We'll kick out those dirty licenses
Ever more, hackers, ever more*

*Join us now and share the software;
You'll be free, hackers, you'll be free
Join us now and share the software;
You'll be free, hackers, you'll be free*

*Hoarders can get piles of money
That is true, hackers, that is true
But they cannot help their neighbors;
That's not good, hackers, that's not good*


## Limitations
This script isn't suitable for very large files, since it loads whole file into memory.