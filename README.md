# Révision AMF

Appli web pour réviser la certification AMF sur téléphone, utilisable hors ligne.

- 2 328 questions de la base commune AMF, classées en 12 thèmes (catégories A et C)
- Révision par thème et sous-thème, séries aléatoires de 10 à 100 questions
- Examen blanc en conditions réelles : 120 questions (33 A + 87 C), 2 h, seuil de 80 % par catégorie
- Progression enregistrée sur l'appareil

## Installer sur le téléphone

Ouvre le site une première fois, puis :
- iPhone (Safari) : Partager → « Sur l'écran d'accueil »
- Android (Chrome) : menu ⋮ → « Installer l'application »

## Fichiers

- `index.html`, `sw.js`, `manifest.webmanifest`, icônes : l'appli publiée
- `questions.json` : la banque de questions
- `source/app.html` + `source/build_pwa.py` : le corps de l'appli et le script qui génère `index.html`, `sw.js` et `manifest.webmanifest`
  (`python3 source/build_pwa.py <dossier contenant index.html=app.html et questions.json> .`)
