# kader-plugins

Ma marketplace de plugins Claude Code.

## Ajouter la marketplace

Dans Claude Code :

```text
/plugin marketplace add kaderdalaa-lang/claude-marketplace
```

En ligne de commande :

```bash
claude plugin marketplace add kaderdalaa-lang/claude-marketplace
```

## Installer un plugin

```text
/plugin install caveman@kader-plugins
/plugin install superpowers@kader-plugins
/plugin install playwright@kader-plugins
/plugin install context7@kader-plugins
/plugin install session-memory@kader-plugins
/plugin install e2e@kader-plugins
```

Ou ouvrir `/plugin`, onglet **Discover**, et choisir un plugin de `kader-plugins`.

## Plugins

| Plugin | Source | Rôle |
|---|---|---|
| caveman | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | Réponses ultra-courtes, moins de tokens |
| superpowers | [obra/superpowers](https://github.com/obra/superpowers) | Skills : TDD, débogage, planification, revue |
| playwright | [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | Pilote un navigateur : clics, formulaires, captures, tests |
| context7 | [upstash/context7](https://github.com/upstash/context7) | Documentation à jour des bibliothèques, par version |
| session-memory | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | Mémoire persistante entre sessions |
| e2e | [tester-army/e2e](https://github.com/tester-army/e2e) | Tests end-to-end web et mobile, écrits et lancés par agent |

## Ajouter un plugin

Ajouter une entrée dans `.claude-plugin/marketplace.json` :

```json
{
  "name": "nom-du-plugin",
  "source": { "source": "url", "url": "https://github.com/auteur/depot.git" },
  "description": "Ce que fait le plugin."
}
```

## Barre de conso (5h + 7 jours, vert/rouge)

Affiche sous la zone de saisie ta consommation Claude : fenêtre de 5 h et semaine.
Vert = tu consommes moins vite que le temps qui passe (tu peux accélérer).
Rouge = plus vite que le temps, ou plus de 85 % (ralentis).

```bash
git clone https://github.com/kaderdalaa-lang/claude-marketplace.git
bash claude-marketplace/statusline/installer-conso.sh
```

Puis relancer Claude Code. Nécessite python3 et un abonnement Claude (Pro/Max) : la barre reste vide après le démarrage, jusqu'à la première réponse.
