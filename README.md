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
```

Ou ouvrir `/plugin`, onglet **Discover**, et choisir un plugin de `kader-plugins`.

## Plugins

| Plugin | Source | Rôle |
|---|---|---|
| caveman | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | Réponses ultra-courtes, moins de tokens |
| superpowers | [obra/superpowers](https://github.com/obra/superpowers) | Skills : TDD, débogage, planification, revue |
| playwright | [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | Pilote un navigateur : clics, formulaires, captures, tests |
| context7 | [upstash/context7](https://github.com/upstash/context7) | Documentation à jour des bibliothèques, par version |

## Ajouter un plugin

Ajouter une entrée dans `.claude-plugin/marketplace.json` :

```json
{
  "name": "nom-du-plugin",
  "source": { "source": "url", "url": "https://github.com/auteur/depot.git" },
  "description": "Ce que fait le plugin."
}
```
