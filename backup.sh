#!/bin/bash
# Script de sauvegarde AEGIS
DATE=$(date +%Y-%m-%d_%Hh%M)
DESTINATION="/home/aegis/backups"
SOURCE="/var/www/html"

# Créer le dossier de destination s'il n'existe pas
mkdir -p $DESTINATION

# Créer l'archive compressée
tar -czf $DESTINATION/backup_site_$DATE.tar.gz $SOURCE

echo "Sauvegarde terminée dans $DESTINATION le $DATE"
