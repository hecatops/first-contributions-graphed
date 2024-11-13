# Contributing To This Repository

## Fork This Repository 
Click on the fork icon on top and fork this repository. This creates a copy of this repository of this repo on your account.


## Cloning This Repository
Click the blue code button and copy the URL (or SSH key if you have created one for your account) and run this on Git Terminal
```bash
git clone "copied url"
```

## Create Your Branch
In the same terminal, change to the repo's directory.
```bash
cd first-contribution-graphed
```

By default, you are on the main branch. So, switch to a new one (-c means create) with any name.
```bash
git switch -c branch-name
```

## Add Your Contribution
Now, navigate to the `data` folder and  open `coding_language.json`. Add your own information to the file, in the same format as the entries above.

For `First_language`, type the name of the first programming language you learnt.
For  `current_language`, type the name of your most used programming language today.
For  `name`, type your name or your nickname.

## Commit Your Contribution
Save the file and on the terminal, add the code to the staging area.
```bash
git add coding_language.json
```

To commit the code, run this code, with the same name as the file.
```bash
git commit -m "Added [name]'s coding languages"
```

Finally, push the changes with
```bash
git push -u origin branch-name
```

## Submitting the Code to this Repository

Open the cloned repository on GitHub and click the `Compare & pull request` button.

Submit the pull request with some comments. The code will be merged manually.

## Congratulations! You Have Completed This Tutorial!
### [You can refer to the cheatsheet for more basic Git commands](docs/Cheatsheet.pdf)
