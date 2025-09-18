# suiviPersoConsoElec

Ce projet permet de suivre et d’analyser sa consommation électrique personnelle. Il offre des outils pour collecter, visualiser, et interpréter les données de consommation afin d’optimiser l’usage de l’électricité et réduire les coûts énergétiques.

## Fonctionnalités

- **Collecte de données** : Récupération automatique ou manuelle des relevés de consommation.
- **Visualisation graphique** : Affichage des consommations sous forme de graphiques (courbes, histogrammes).
- **Analyse statistique** : Outils pour calculer la consommation moyenne, détecter les pics, comparer par période.
- **Export des données** : Possibilité d’exporter les résultats au format CSV ou PDF.
- **Interface web** : Application web simple pour consulter ses données et rapports.

## Installation

1. **Cloner le dépôt :**
   ```bash
   git clone https://github.com/Valyfaliana/suiviPersoConsoElec.git
   cd suiviPersoConsoElec
   ```
2. **Créer un environnement virtuel :**
   ```bash
   python -m venv venv
   source venv/bin/activate  # ou `venv\Scripts\activate` sous Windows
   ```
3. **Installer les dépendances :**
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

- Pour lancer l’application :
  ```bash
  python main.py
  ```
- Accéder à l’interface via [http://localhost:5000](http://localhost:5000) (si une interface web est incluse).

## Structure du projet

```
suiviPersoConsoElec/
├── app/               # Jeux de données et exports
├── ...
├── dist/          # Contient le fichier .exe
├── main.py             # Script principal
├── README.md           # Ce fichier
├── requirements.txt    # Dépendances Python
└── ...
```

## Technologies utilisées

- **Python** (analyses, backend)
- **HTML** (interface web)
- **TeX** (génération de rapports PDF)

## Contribuer

Les contributions sont les bienvenues ! N’hésitez pas à ouvrir une issue ou proposer une pull request.

## Auteur

- [Valyfaliana](https://github.com/Valyfaliana)

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus d’informations.
