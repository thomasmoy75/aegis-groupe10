import socket
import subprocess
import json

def check_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex(('127.0.0.1', port))
    sock.close()
    return "Ouvert" if result == 0 else "Ferme"

def check_service(service_name):
    try:
        # Vérifie si le service est actif [cite: 90, 304]
        output = subprocess.check_output(['systemctl', 'is-active', service_name], text=True).strip()
        return "Actif" if output == 'active' else "Inactif"
    except subprocess.CalledProcessError:
        return "Inactif"

def main():
    print("--- Lancement de l'audit automatisé AEGIS ---")
    
    # Inventaire des ports [cite: 91, 305]
    ports_to_check = [22, 80, 2222]
    ports_status = {f"Port_{p}": check_port(p) for p in ports_to_check}
    
    # Inventaire des services actifs [cite: 90, 304]
    services_to_check = ['ssh', 'ufw', 'fail2ban', 'apache2']
    services_status = {s: check_service(s) for s in services_to_check}
    
    # Rassemblement des données pour l'export [cite: 92, 306]
    rapport = {
        "Projet": "AEGIS - Audit TechSud",
        "Ports_Reseau": ports_status,
        "Services_Systeme": services_status
    }
    
    # Export du résultat en JSON [cite: 92, 306]
    with open('rapport_audit.json', 'w') as f:
        json.dump(rapport, f, indent=4)
        
    print("Audit terminé ! Le fichier 'rapport_audit.json' a été généré.")

if __name__ == "__main__":
    main()
