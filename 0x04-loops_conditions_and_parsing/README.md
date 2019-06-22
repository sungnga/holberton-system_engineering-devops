# 0x04. Loops, conditions and parsing

## Learning Objectives
* How to create SSH keys
* What is the advantage of using  #!/usr/bin/env bash over #!/bin/bash
* How to use while, until and for loops
* How to use if, else, elif and case condition statements
* How to use the cut command
* What are files and other comparison operators, and how to use them

### Resources
* Loops sample
* Variable assignment and arithmetic
* Comparison operators
* File test operators
* Make your scripts portable

### man or help
* env
* cut
* for
* while
* until
* if

### Requirements
* All your files will be interpreted on Ubuntu 14.04 LTS
* All your files should end with a new line
* All your Bash script files must be executable
* You are not allowed to use awk
* Your Bash script must pass Shellcheck (version 0.3.3-1~ubuntu14.04.1 via apt-get) without any error
* The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
* The second line of all your Bash scripts should be a comment explaining what is the script doing

### Shellcheck
[Shellcheck](https://github.com/koalaman/shellcheck) is a tool that will help you write proper Bash scripts. It will make recommendations on your syntax and semantics and provide advice on edge cases that you might not have thought about. Shellcheck is your friend! All your Bash scripts must pass Shellcheck without any error or you will not get any points on the task.

[To install](https://github.com/koalaman/shellcheck#installing)
* On command prompt: sudo apt-get shellcheck

---

## TASKS

### [0. Create a SSH RSA key pair](./0-RSA_public_key.pub)
Read for this task:
* [Linux and Mac OS users](https://askubuntu.com/questions/61557/how-do-i-set-up-ssh-authentication-keys)
* [Windows users](https://support.rackspace.com/how-to/generating-rsa-keys-with-ssh-puttygen/)

man: `ssh-keygen`

You will soon have to manage your own [servers](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_web_server) hosted on remote [data centers](https://www.youtube.com/watch?v=iuqXFC_qIvA&feature=youtu.be&t=46). We need to set them up with your RSA public key so that you can access them via SSH.

Create a RSA key pair.

Requirements:
* Share your public key in your answer file `0-RSA_public_key.pub`
* Fill the `SSH public key` field of your intranet profile with the public key you just generated
* Keep the private key to yourself in a secure location, you will use it later to connect to your servers using SSH. Some storing ideas are Dropbox, Google Drive, password manager, USB key. Failing to do so will prevent you to access your servers, which will prevent you from doing your projects
* If you decide to add a passphrase to your key, make sure to save this passphrase in a secure location, you will not be able to use your keys without the passphrase
SSH and RSA keys will be covered in depth in a later project.

Directory: `0x04-loops_conditions_and_parsing`
File: `0-RSA_public_key.pub`

### [1. For Holberton School loop](./1-for_holberton_school)
* Write a Bash script that displays Holberton School 10 times.


### [2. While Holberton School loop](./2-while_holberton_school)
* Write a Bash script that displays Holberton School 10 times.


### [3. Until Holberton School loop](./3-until_holberton_school)
* Write a Bash script that displays Holberton School 10 times.


### [4. If 9, say Hi!](./4-if_9_say_hi)
* Write a Bash script that displays Holberton School 10 times, but for the 9th iteration, displays Holberton School and then Hi on a new line.


### [5. 4 bad luck, 8 is your chance](./5-4_bad_luck_8_is_your_chance)
* Write a Bash script that loops from 1 to 10 and:


### [6. Superstitious numbers](./6-superstitious_numbers)
* Write a Bash script that displays numbers from 1 to 20 and:


### [7. Clock](./7-clock)
* Write a Bash script that displays the time for 12 hours and 59 minutes:


### [8. For ls](./8-for_ls)
* Write a Bash script that displays:


### [9. To file, or not to file](./9-to_file_or_not_to_file)
* Write a Bash script that gives you information about the holbertonschool file.


### [10. FizzBuzz](./10-fizzbuzz)
* Write a Bash script that displays numbers from 1 to 100.


### [11. Read and cut](./100-read_and_cut)
* help: read


### [12. Tell the story of passwd](./101-tell_the_story_of_passwd)
* 


### [13. Let's parse Apache logs](./102-lets_parse_apache_logs)
* 


### [14. Dig the data](./103-dig_the-data)
* Now that you’ve parsed the Apache log file, let’s sort the data so you can get a better idea of what is going on.

---

## Author
* **Nga La** - [sungnga](https://github.com/sungnga)