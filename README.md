<div align="center">

# 🚀 devspace-AI

### PREPARE YOUR 🍏 Mac FOR DEVELOPMENT </br> with GitHub Copilot/agent workflows

![devspace-ai banner](docs/devspace-ai.png)

> **[version 🇫🇷 française](./ALIRE.md)**

</div>

<table align="center">
<tr>
<td width="33%" align="center">
<h3>🎯</h3>
Follow this guide<br/>and <strong>Copilot</strong>
</td>
<td width="33%" align="center">
<h3>⚡</h3>
Type <code>/start</code><br/>~30min to ready
</td>
<td width="33%" align="center">
<h3>🔰</h3>
No prior knowledge<br/>just follow the guide
</td>
</tr>
</table>



<div align="center">

## 🏁 <span style="color: #2ea44f;"> GET READY in 6 STEPS</span>

</div>

### <span style="color: #2da44e;">1️⃣ Create GitHub account & activate Copilot</span>

Create an account on [github.com](https://github.com) and activate your [Copilot subscription](https://github.com/features/copilot/plans) — you can use the free plan

### <span style="color: #2da44e;">2️⃣ Check curl</span>

`curl` downloads files from the internet via terminal — usually pre-installed on Mac

```sh
curl --version
# should show: curl 8.7.1 or higher
```

If `curl` isn't installed, see [curl.se](https://curl.se)

### <span style="color: #2da44e;">3️⃣ Install Homebrew</span>

Mac's package manager (like an app store for developers)

```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

⏱️ Takes ~10 min

**After installation**, add Homebrew to your PATH (the installer will show these commands):

```sh
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

### <span style="color: #2da44e;">4️⃣ Install VS Code</span>

Your code editor — Copilot lives here

```sh
brew install --cask visual-studio-code
```

### <span style="color: #2da44e;">5️⃣ Clone devspace-ai</span>

Create a folder and download this project:

```sh
mkdir -p ~/Developer/devspace-ai
cd ~/Developer/devspace-ai
git clone https://github.com/punkyard/devspace-ai.git .
```

**Note:** if `git` wasn't installed yet, install it first:

```sh
brew install git
```

### <span style="color: #2da44e;">6️⃣ Open in VS Code and say `/start`</span>

- launch VS Code
- click **File** > **Open folder...**
- navigate to `~/Developer/devspace-ai` and click **Open**
- click your profile icon (bottom left) and sign in with GitHub
- open the chat box (`Alt+Cmd+B` or `Option+Command+B`)
- type: `/start`

---

<details>
<summary><strong>🤔 What is all this stuff by the way?</strong></summary>

### <span style="color: #0969da;">git</span>
<strong style="color:#0969da;">What:</strong> version control — tracks every change you make to code  
<strong style="color:#0969da;">Why:</strong> collaborate with others, undo mistakes, keep history, publish on GitHub  
<strong style="color:#0969da;">In practice:</strong> save your work at important moments, go back if something breaks, share code with teammates

### <span style="color: #0969da;">Node.js + npm</span>
<strong style="color:#0969da;">What:</strong> JavaScript runtime + package manager (like an app store for code libraries)  
<strong style="color:#0969da;">Why:</strong> many modern projects need it; npm installs pre-made code others wrote  
<strong style="color:#0969da;">In practice:</strong> run JavaScript code on your Mac, download useful tools instead of writing them from scratch

### <span style="color: #0969da;">NVM</span>
<strong style="color:#0969da;">What:</strong> Node Version Manager — lets you switch between different Node.js versions  
<strong style="color:#0969da;">Why:</strong> different projects need different versions  
<strong style="color:#0969da;">In practice:</strong> some projects work with Node 16, others need Node 18 — NVM lets you switch without breaking anything

### <span style="color: #0969da;">GitHub Copilot</span>
<strong style="color:#0969da;">What:</strong> AI assistant that writes code with you  
<strong style="color:#0969da;">Why:</strong> explains code, suggests solutions, helps you learn faster  
<strong style="color:#0969da;">In practice:</strong> you describe what you want, Copilot writes it, you learn how it works

### <span style="color: #0969da;">MCP Servers</span>
<strong style="color:#0969da;">What:</strong> Model Context Protocol — connections that give Copilot superpowers  
<strong style="color:#0969da;">Why:</strong> search the web, read docs, access tools — all inside VS Code  
<strong style="color:#0969da;">In practice:</strong> ask Copilot a question, it searches the web for the answer and explains it to you — no tab-switching needed

**MCP servers configured in this project:**
- **Brave Search MCP:** real-time web search from VS Code
- **Context7 MCP:** instant access to documentation for libraries and frameworks

### <span style="color: #0969da;">Homebrew</span>
<strong style="color:#0969da;">What:</strong> macOS package manager  
<strong style="color:#0969da;">Why:</strong> installs developer tools easily  
<strong style="color:#0969da;">In practice:</strong> instead of downloading installers manually, use `brew install` commands

### <span style="color: #0969da;">curl</span>
<strong style="color:#0969da;">What:</strong> command-line tool for transferring data with URLs  
<strong style="color:#0969da;">Why:</strong> downloads files and scripts from the internet via terminal  
<strong style="color:#0969da;">In practice:</strong> used to install Homebrew and other tools

</details>

---

<div align="center">

## 📋 <span style="color: #1f6feb;">after you `/start`</span>

### **Copilot guides you through:**

</div>

<table>
<tr>
<td width="50%" align="left" style="text-align:left; vertical-align:top;">

1. 💬 **questions about your Mac**  
   <sub>identifies your environment, stored in `context/environment.md`</sub>

2. 🛠️ **install Git, Node.js (LTS), and NVM**  
   <sub>version manager for Node via installer script</sub>

3. 🔑 **create API keys**  
   <sub>for Brave Search MCP ([free](https://brave.com/search/api/)) and Context7 MCP ([free, optional](https://context7.com))</sub>

</td>

<td width="50%" align="left" style="text-align:left; vertical-align:top;">

4. ⚡ **set up MCP servers**  
   <sub>Brave Search (web search) + Context7 (docs access)</sub>

5. 🧪 **test your first prompt**  
   <sub>write a prompt, see Copilot work</sub>

6. ✅ **done!**  
   <sub>your Mac is production-ready</sub>

</td>
</tr>
</table>

<div align="center">

🔒 Each step asks for your confirmation before running: **You're in control.**

</div>

---

<div align="center">

## 💡 <span style="color: #8957e5;">What you'll be able to do next</span>

</div>

<table>
<tr>
<td width="33%" valign="top">

### <span style="color: #8250df;">🚀 Start Building</span>
Clone [boilerspace-ai](https://github.com/punkyard/boilerspace-ai) templates for AI-assisted projects

### <span style="color: #8250df;">📥 Download & Study</span>
Clone projects from GitHub, see how real code works, copy patterns

</td>

<td width="33%" valign="top">

### <span style="color: #8250df;">🌐 Search & Code</span>
Web search in your editor with Brave MCP, no tab-switching

### <span style="color: #8250df;">🤝 Code with AI</span>
Copilot explains each line as you write

</td>

<td width="33%" valign="top">

### <span style="color: #8250df;">👥 Join & Learn</span>
Communities like [Dev.to](https://dev.to), [Hashnode](https://hashnode.com), local meetups

### <span style="color: #8250df;">📰 Stay Updated</span>
Follow [daily.dev](https://daily.dev), [Code Report](https://www.youtube.com/@CodeReport)

</td>
</tr>
</table>

---

<div align="center">

## 🔒 <span style="color: #cf222e;">Important notes</span>

</div>

- <strong style="color:#bf8700;">API keys are safe:</strong> we use VS Code inputs and environment variables (never committed to GitHub)
- <strong style="color:#bf8700;">you stay in control:</strong> each step asks for your confirmation
- <strong style="color:#bf8700;">open source:</strong> see `.github/copilot-instructions.md` for the full ruleset
- <strong style="color:#bf8700;">canonical docs:</strong> all Copilot rules live in `.github/` (the Single Source of Truth)
- <strong style="color:#bf8700;">file structure:</strong> folder structure and instruction files are indexed in `.github/copilot-instructions.md`

---

<div align="center">

## 🐛 <span style="color: #d1242f;">Found an issue?</span>

</div>

- <strong style="color:#bf8700;">problems during setup?</strong> [open an issue](https://github.com/punkyard/devspace-ai/issues)
- <strong style="color:#bf8700;">have an idea?</strong> suggest it in [Discussions](https://github.com/punkyard/devspace-ai/discussions)
- <strong style="color:#bf8700;">roadmap:</strong> see [GitHub Issues](https://github.com/punkyard/devspace-ai/issues?q=is%3Aissue+is%3Aopen+label%3Aenhancement) for planned features

---

<div align="center">

License: GNU Affero General Public License v3 (AGPLv3) — see `LICENSE`</br> © 2025 Gouteron

<sub>made with ⏳ by <a href="https://github.com/punkyard">punkyard</a></sub>

</div>
