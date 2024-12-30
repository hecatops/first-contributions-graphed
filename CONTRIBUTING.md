# Contributing To This Repository

Welcome! Contributing here is not just rewarding—it's also fun! Follow this guide to make your first pull request with ease. 😃

---

## ✨ Step 1: Fork This Repository

Click the **Fork** icon at the top-right of this repository page. This action creates a shiny, new copy of this repository in your GitHub account. (Isn't that cool?)

---

## 🔄 Step 2: Clone Your Fork

Once you've forked it, click the blue **Code** button and copy the URL (or the SSH key if you prefer).

Now, fire up your terminal and run:

```bash
git clone "your-copied-url"
```

Watch as Git pulls down a copy to your local machine. You're officially on your way! 🏋️‍♂️

---

## ⚛ Step 3: Create Your Own Branch

Time to branch out—literally! First, navigate to the project directory:

```bash
cd first-contribution-graphed
```

Now create and switch to your very own branch. Pick a fun name for it (maybe `add-cool-feature`?):

```bash
git switch -c branch-name
```

---

## 🌐 Step 4: Add Your Contribution

Let’s get creative! Navigate to the `data` folder and open `coding_language.json`. Add your own information in this format:

```json
{
  "name": "Your Name or Nickname",
  "first_language": "Your first programming language",
  "current_language": "Your most-used programming language"
}
```

Example:

```json
{
  "name": "Alex",
  "first_language": "Python",
  "current_language": "JavaScript"
}
```

Save your changes. You're now part of something special!

---

## 🔄 Step 5: Commit Your Changes

First, stage your changes:

```bash
git add coding_language.json
```

Then commit them with a meaningful message:

```bash
git commit -m "Added [Your Name's] coding languages"
```

Finally, push your branch to your fork:

```bash
git push -u origin branch-name
```

You’re almost done! Hang tight.

---

## 🎨 Step 6: Submit a Pull Request

Go to your forked repository on GitHub. You should see a **Compare & pull request** button—click it! Add a friendly description of what you’ve contributed. Then submit your pull request.

The maintainers will review it, and before you know it, your contribution will be merged. High five! 🙌

---

## 🎉 Congratulations!

You just made your first contribution to this repository. Go celebrate—you’ve earned it! 🎉

Want to learn more Git commands? Check out our [Git Cheatsheet](docs/Cheatsheet.pdf). It’s your handy guide to mastering version control like a pro.
