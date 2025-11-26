<div align="center">

# 🚀 devspace-AI

### PRÉPARE VOTRE 🍏 Mac POUR LE DÉVELOPPEMENT </br> avec l'assistant IA GitHub Copilot

🎯 suivre ce guide et **Copilot**

⚡ taper `/start` ~30min pour être prêt

🔰 aucune connaissance préalable

### 🇫🇷 [🇬🇧](../README.md)

![devspace-ai banner](../docs/devspace-ai.png)

# 🏁 C'EST PARTI 🏁

</div>

### 1️⃣ Créer un compte GitHub et activer Copilot

- créer un compte sur [github.com](https://github.com) et activer l'abonnement [Copilot](https://github.com/features/copilot/plans) — pour utiliser le plan gratuit

### 2️⃣ Vérifier `curl`

- `curl` télécharge des fichiers depuis Internet via le terminal — généralement préinstallé sur Mac

```sh
curl --version
# devrait afficher: curl 8.7.1 ou plus
```

- Si `curl` n'est pas installé, voir [curl.se](https://curl.se)

### 3️⃣ Installer `homebrew`

- Le gestionnaire de paquets macOS (comme un store pour développeurs)

```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

- ⏱️ Prend ~10 min

- **après l'installation**, ajouter Homebrew au PATH du système (l'installateur affichera ces commandes) :

```sh
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

### 4️⃣ Installer `Visual Studio Code`

-un éditeur de code qui intègre Copilot

```sh
brew install --cask visual-studio-code
```

### 5️⃣ Cloner `devspace-AI`

- créer un dossier et télécharger ce projet :

```sh
mkdir -p ~/Developer/devspace-AI
cd ~/Developer/devspace-AI
git clone https://github.com/punkyard/devspace-ai.git .
```

- **remarque :** si `git` n'est pas encore installé, l'installer d'abord :

```sh
brew install git
```

### 6️⃣ Ouvrir VS Code et taper `/start`

- lancer VS Code
- cliquer sur **File** > **Open folder...**
- naviguer vers `~/Developer/devspace-AI` et cliquer sur **Open**
- cliquer sur l'icône de profil (en bas à gauche) et se connecter avec GitHub
- ouvrir la zone de chat (`Alt+Cmd+B` ou `Option+Cmd+B`)
- taper : `/start`


<details>
<summary><strong>🤔 C'est quoi tout ça ?</strong></summary>

### git
- contrôle de version — enregistre chaque modification du code  
- pour collaborer, annuler des erreurs, garder l'historique, publier sur GitHub  
- **en pratique :** sauvegarder le travail à des moments importants, revenir en arrière si nécessaire, partager le code

### Node.js + npm
- runtime JavaScript + gestionnaire de paquets  
- de nombreux projets modernes en dépendent  
- **en pratique :** exécuter du JavaScript sur Mac, installer des outils existants

### NVM
- Node Version Manager — changer facilement de version Node.js  
- car différents projets demandent différentes versions  
- **en pratique :** basculer entre Node 16, 18, etc

### GitHub Copilot
- assistant IA qui aide à écrire du code  
- il propose, explique, accélère la rédaction de code  
- **en pratique :** décrire ce qu'on veut, Copilot propose du code

### serveurs MCP
- Model Context Protocol — connecteurs qui donnent des capacités étendues à Copilot  

**MCP configurés dans ce projet :**
- **Time MCP :** timestamps UTC canoniques et conversions de fuseaux horaires (pas de clé API requise)
- **Brave Search MCP :** recherche web en temps réel depuis VS Code
- **Context7 MCP :** accès instantané à la documentation des bibliothèques

### Homebrew
- gestionnaire de paquets macOS  
- pour installer et mettre à jour logiciels et outils facilement
- **en pratique :** utiliser `brew install` au lieu de télécharger manuellement

### curl
- outil en ligne de commande pour transférer des données via des URLs  
- télécharger des scripts et fichiers depuis le terminal  
- **en pratique :** utile pour installer Homebrew et autres outils

</details>


<div align="center">

# 📋 après `/start`

</div>

### **Copilot vous guide**

1. 💬 **questions sur votre Mac**  
   <sub>identifie l'environnement, stocké dans `context/environment.md`</sub>

2. 🛠️ **installer Git, Node.js (LTS) et NVM**  
   <sub>installe via script le gestionnaire de versions Node</sub>

3. 🔑 **créer des clefs API**  
   <sub>pour Brave Search MCP ([gratuit](https://brave.com/search/api/)) et Context7 MCP ([gratuit, optionnel](https://context7.com))</sub>

4. ⚡ **configurer les MCP**  
   <sub>Brave Search (recherche web) + Context7 (accès docs)</sub>

5. 🧪 **rédiger un premier prompt**  
   <sub>rédiger un prompt, observer Copilot en action</sub>

6. ✅ **terminé !**  
   <sub>votre Mac est prêt pour le développement</sub>

🔒 chaque étape demande confirmation avant d'exécuter pour **garder le contrôle**.


<div align="center">

# 💡 Que faire ensuite ?

</div>

> 🚀 **commencer à construire** : cloner le template [boilerspace-AI](https://github.com/punkyard/boilerspace-ai)
>
> 🌐 **rechercher & coder** : recherche web dans l'éditeur avec Brave MCP, pas de changement d'onglet
>
> 👥 **rejoindre & apprendre** : communautés comme [Dev.to](https://dev.to), [Hashnode](https://hashnode.com)
>
> 📥 **télécharger & étudier** : cloner des projets GitHub pour apprendre avec des exemples réels
>
> 🤝 **coder avec l'IA** : Copilot explique chaque ligne ou code à la demande
>
> 📰 **rester informé** : en suivant [daily.dev](https://daily.dev), [Code Report](https://www.youtube.com/@CodeReport)


<div align="center">

## 🔒 Notes importantes

</div>

- **Les clefs API sont sûres** : nous utilisons les inputs VS Code et variables d'environnement (jamais commit)
- **vous gardez le contrôle** : chaque étape demande confirmation
- **open source** : voir `.github/copilot-instructions.md` pour le référentiel de règles
- **docs canoniques** : toutes les règles Copilot se trouvent dans `.github/`

<div align="center">

## 🐛 Un bug ?

</div>

- **problème lors de la configuration ?** [créer un ticket](https://github.com/punkyard/devspace-ai/issues)
- **une idée ?** la proposer dans [Discussions](https://github.com/punkyard/devspace-ai/discussions)
- **feuille de route** : voir [Issues](https://github.com/punkyard/devspace-ai/issues?q=is%3Aissue+is%3Aopen+label%3Aenhancement)

---

<div align="center">

GNU Affero General Public License v3 (AGPLv3) — voir [LICENSE](./LICENSE-FR.md)</br>

réalisé avec ⏳ par <a href="https://github.com/punkyard">punkyard</a>

</div>
