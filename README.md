# Stuyvesant Spectator Website 2017

minion: http://fontsgeek.com/search?q=minion+pro
## Bugs
- navbar collapse is glitchy on tall screens
## Standard dependency workflow
*Do NOT check dependencies into the repo*
- Create a virtual environment outside the repo (or inside, as long as you
do not check it into the repo)
- When you add a new dependency:
  `pip freeze > requirements.txt`
- When you want to install the new dependencies:
  `pip install -r requirements.txt`
- THE ONLY THING ADDED TO THE REPO SHOULD BE `requirements.txt`


## Tips for Deployment

- Do not check db files into the repo
- Deploy early
- Use automated deployment scripts
  - A good way to automate deployment is through git hooks
- Do not use spaces, hyphens or slashes in the app name

## Team

| Photo |  Name  |  Role  | Programming Languages  |
|-------|--------|--------|------------------------|
| <img src="http://nicholasyang.com/images/Headshot.jpg" align="left" height="100" > | Nicholas Yang | Project Consultant | Python, Ruby, JavaScript, C++, SQL |
| <img src="http://nicholasyang.com/images/Headshot.jpg" align="left" height="100" > | Jason Kao | Editor | Python, Ruby, JavaScript, C++, SQL |
